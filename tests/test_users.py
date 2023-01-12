import pytest
from jose import jwt
from app import schemas
from app.config import settings

def test_root(client):
    res = client.get("/")
    assert res.status_code == 200

def test_login_user(test_user, client):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']})
    
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("userid")

    assert id == test_user['id']
    assert res.status_code == 200
    assert login_res.token_type == "bearer"

# def test_fail_login(test_user, client):
#     res = client.post("/login", data={"username": test_user['email'], "password": "tacos"})
#     assert res.status_code == 403
#     assert res.json().get('detail') == 'Identifiants invalides'
