from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post,user

# Automatic documentation (Swagger UI):
# http://127.0.0.1:8000/docs/
# http://127.0.0.1:8000/redoc/

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur mon API"}

while True:
    try: # To-Do: vars!
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='2YuHHakD7fy6tK88aHm2jd7cuKZMFbjsEBYoYGZtMHtX8BPBsLedxEx3mxvANaNWM8zQdqvPjE7oXZzp37KwhRv7iAd3LNwEVjJj58A27GPHeBPvwyBjWfNQwNvygg79',
        cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was sucessful!")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)
