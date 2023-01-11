from app import schemas
from .database import client, session

def test_create_user(client):
    res = client.post("/users/", json={"email": "pizza@pizza.it", "password": "pepperoni"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == ""
    assert res.status_code == 201
