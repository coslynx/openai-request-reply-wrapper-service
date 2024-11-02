from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, validator
from typing import Optional
import os
import requests
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .api.routes.requests import router as requests_router
from .api.dependencies.openai import get_openai_client
from .api.services.request_service import get_db, create_request, create_user
from .models.request import Request
from .models.user import User

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# Database setup (PostgreSQL with SQLAlchemy)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define your models here

# Example request model
class RequestModel(BaseModel):
    prompt: str
    model: str = "text-davinci-003"
    temperature: float = 0.7

@app.post("/requests")
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

# ... additional routes and functions ...

# Start the server (using uvicorn)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,  # Enable auto-reload for development
    )