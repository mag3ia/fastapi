from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from alembic import command
from app.database import get_db
from app.main import app
from app import schemas
from app.config import settings
from app.database import Base

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Swap database, will get a different session object:
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] == override_get_db


@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # command.upgrade("head")
    # command.downgrade("base")
    yield TestClient(app)


def test_create_user(client):
    res = client.post("/users/", json={"email": "pizza@pizza.it", "password": "pepperoni"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == ""
    assert res.status_code == 201
