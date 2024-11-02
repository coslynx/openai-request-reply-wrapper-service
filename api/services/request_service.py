from typing import Optional
from sqlalchemy.orm import Session

from .models.request import Request
from .models.user import User  # Import for user history management (if implemented)

# Dependency function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_request(db: Session, request: RequestModel, user_id: int):
    """
    Creates a new database entry for a user request.

    Args:
        db (Session): The SQLAlchemy database session.
        request (RequestModel): The user request data.
        user_id (int): The ID of the user making the request.

    Returns:
        Request: The newly created database entry for the request.
    """
    # Implement logic to interact with OpenAI API and get response 
    # ...

    # Create database entry for the request
    db_request = Request(
        user_id=user_id,
        prompt=request.prompt,
        model=request.model,
        parameters=request.parameters,
        response=response_from_openai,  # Assuming response is processed in this function
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

def create_user(db: Session, username: str, password: str):
    """
    Creates a new user in the database.

    Args:
        db (Session): The SQLAlchemy database session.
        username (str): The username for the new user.
        password (str): The password for the new user.

    Returns:
        User: The newly created database entry for the user.
    """
    # Implement password hashing using bcrypt
    # ...

    db_user = User(
        username=username,
        password=hashed_password,
        # ... any additional user data ...
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user