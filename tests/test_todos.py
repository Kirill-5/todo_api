import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200

    login_response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    token = login_response.json()["access_token"]

    response = client.post("/todos", json={"title": "Test todo"} , headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "id" in response.json()



def test_get_todos():
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200

    login_response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    token = login_response.json()["access_token"]

    response = client.post("/todos/", json={"title": "Test todo"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "id" in response.json()

    response = client.get("/todos/", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200

    todos = response.json()
    assert isinstance(todos, list)
    assert len(todos) > 0
    assert todos[0]["title"] == "Test todo"


def test_update_todo():
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200

    login_response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    token = login_response.json()["access_token"]

    response = client.post("/todos/", json={"title": "Test todo"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "id" in response.json()

    todo_id = response.json()["id"]

    response = client.patch(f"/todos/{todo_id}", json={"completed": True}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["completed"] is True



def test_delete_todo():
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200

    login_response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()

    token = login_response.json()["access_token"]

    response = client.post("/todos/", json={"title": "Test todo"}, headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert "id" in response.json()

    todo_id = response.json()["id"]

    response = client.delete(f"/todos/{todo_id}", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["message"] == "deleted"