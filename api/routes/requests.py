from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, validator
from typing import Optional

from .api.dependencies.openai import get_openai_client
from .api.services.request_service import get_db, create_request
from .models.request import Request

router = APIRouter()

# Example request model
class RequestModel(BaseModel):
    prompt: str
    model: str = "text-davinci-003"
    temperature: float = 0.7

@router.post("/requests", tags=["Requests"])
async def process_request(request: RequestModel, db: SessionLocal = Depends(get_db)):
    try:
        openai_client = get_openai_client()
        response = openai_client.chat_completion.create(
            model=request.model,
            messages=[
                {"role": "user", "content": request.prompt}
            ],
            temperature=request.temperature,
        )
        db_request = Request(
            user_id=1,  # Replace with user ID if authentication is implemented
            prompt=request.prompt,
            model=request.model,
            parameters={"temperature": request.temperature},
            response=response["choices"][0]["message"]["content"],
        )
        db.add(db_request)
        db.commit()
        db.refresh(db_request)
        return {"response": response["choices"][0]["message"]["content"]}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))