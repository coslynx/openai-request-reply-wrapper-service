import pytest
from fastapi.testclient import TestClient
from api.routes.requests import router
from api.dependencies.openai import get_openai_client
from api.services.request_service import get_db, create_request, create_user
from models.request import Request
from models.user import User
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class TestRequests:
    @pytest.fixture(scope="function")
    def client(self):
        app = FastAPI()
        app.include_router(router)
        yield TestClient(app)

    @pytest.fixture(scope="function")
    def db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @pytest.fixture(scope="function")
    def openai_client(self, monkeypatch):
        def mock_create(*args, **kwargs):
            return {"choices": [{"message": {"content": "Mock response"}}]}
        monkeypatch.setattr(get_openai_client().chat_completion, 'create', mock_create)
        yield get_openai_client()

    def test_process_request_valid_data(self, client, db, openai_client):
        response = client.post("/requests", json={"prompt": "Hello, world!", "model": "text-davinci-003", "temperature": 0.7})
        assert response.status_code == 200
        assert response.json() == {"response": "Mock response"}
        assert db.query(Request).count() == 1

    def test_process_request_invalid_data(self, client, db, openai_client):
        response = client.post("/requests", json={"prompt": "Hello, world!"})
        assert response.status_code == 422

    def test_process_request_openai_error(self, client, db, openai_client, monkeypatch):
        def mock_create(*args, **kwargs):
            raise Exception("OpenAI API error")
        monkeypatch.setattr(get_openai_client().chat_completion, 'create', mock_create)
        response = client.post("/requests", json={"prompt": "Hello, world!", "model": "text-davinci-003", "temperature": 0.7})
        assert response.status_code == 500

    def test_process_request_database_error(self, client, db, openai_client, monkeypatch):
        def mock_add(self, *args, **kwargs):
            raise Exception("Database error")
        monkeypatch.setattr(db, 'add', mock_add)
        response = client.post("/requests", json={"prompt": "Hello, world!", "model": "text-davinci-003", "temperature": 0.7})
        assert response.status_code == 500