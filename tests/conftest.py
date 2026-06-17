import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.database import SessionLocal
from app.models.user import User
from app.models.todo import Todo

@pytest.fixture(autouse=True)
def clean_db():
    """Очищает таблицы users и todo после каждого теста"""
    db = SessionLocal()
    try:
        # Удаляем всё в правильном порядке (сначала todo, потом users)
        db.query(Todo).delete()
        db.query(User).delete()
        db.commit()
    finally:
        db.close()

@pytest.fixture
def client():
    """Возвращает TestClient для тестов"""
    return TestClient(app)