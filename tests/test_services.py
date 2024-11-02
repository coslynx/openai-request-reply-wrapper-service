import pytest
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

from .models.request import Request
from .models.user import User

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class TestRequestService:
    @pytest.fixture(scope="function")
    def db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def test_create_request(self, db):
        request_data = {
            "user_id": 1,
            "prompt": "Hello, world!",
            "model": "text-davinci-003",
            "parameters": {"temperature": 0.7},
            "response": "This is a test response.",
        }
        request = Request(**request_data)
        db.add(request)
        db.commit()
        db.refresh(request)
        assert request.prompt == request_data["prompt"]
        assert request.model == request_data["model"]
        assert request.response == request_data["response"]

    def test_get_request_by_id(self, db):
        request_data = {
            "user_id": 1,
            "prompt": "Hello, world!",
            "model": "text-davinci-003",
            "parameters": {"temperature": 0.7},
            "response": "This is a test response.",
        }
        request = Request(**request_data)
        db.add(request)
        db.commit()
        db.refresh(request)
        fetched_request = db.query(Request).get(request.id)
        assert fetched_request.prompt == request_data["prompt"]
        assert fetched_request.model == request_data["model"]
        assert fetched_request.response == request_data["response"]

    def test_update_request(self, db):
        request_data = {
            "user_id": 1,
            "prompt": "Hello, world!",
            "model": "text-davinci-003",
            "parameters": {"temperature": 0.7},
            "response": "This is a test response.",
        }
        request = Request(**request_data)
        db.add(request)
        db.commit()
        db.refresh(request)
        request.prompt = "Updated prompt"
        db.commit()
        db.refresh(request)
        assert request.prompt == "Updated prompt"

    def test_delete_request(self, db):
        request_data = {
            "user_id": 1,
            "prompt": "Hello, world!",
            "model": "text-davinci-003",
            "parameters": {"temperature": 0.7},
            "response": "This is a test response.",
        }
        request = Request(**request_data)
        db.add(request)
        db.commit()
        db.refresh(request)
        db.delete(request)
        db.commit()
        assert db.query(Request).get(request.id) is None

    def test_create_user(self, db):
        user_data = {"username": "testuser", "password": "testpassword"}
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        assert user.username == user_data["username"]