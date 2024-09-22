import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal
from app.models.user import UserModel

client = TestClient(app)

@pytest.fixture
def db_session():
    db = SessionLocal()
    yield db
    db.close()

def test_create_user(db_session):
    response = client.post("/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_read_user(db_session):
    user = UserModel(name="Jane Doe", email="jane@example.com")
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    response = client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"
