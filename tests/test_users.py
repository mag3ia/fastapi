import pytest
from app import schemas
from .database import client, session

@pytest.fixture
def test_user(client):
    user_data = {"email": "pizza@pizza.it", "password": "pepperoni"}
    res = client.post("/users/", json=user_data)

    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

def test_root(client):
    res = client.get("/")
    assert res.status_code == 200

# def test_create_user(client):
#     res = client.post("/users/", json={"email": "pizza@pizza.it", "password": "pepperoni"})
#     new_user = schemas.UserOut(**res.json())
#     assert new_user.email == "pizza@pizza.it"
#     assert res.status_code == 201

def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    assert res.status_code == 200