import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



def test_register_success(client):
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200

def test_register_fail():
    client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    response = client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 400

def test_login_success():
    client.post("/auth/register", json={
        "username": "admin2",
        "password": "admin123"
    })
    response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "admin123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_fail():
    response = client.post("/auth/login", json={
        "username": "admin2",
        "password": "wrong"
    })
    assert response.status_code == 400