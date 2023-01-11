from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    print(res.json().get('message'))
    assert res.json().get('message') == 'Bienvenue sur mon API'
    assert res.status_code == 200
