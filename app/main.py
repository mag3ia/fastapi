from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


# Automatic documentation :
# http://127.0.0.1:8000/docs/
# http://127.0.0.1:8000/redoc/

# Creation des tables (conrespondant à models.py)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Post(BaseModel):  
    title: str
    content: str
    published: bool = True
#     rating: Optional[int] = None

@app.get("/")
def root():
    return {"message": "Bienvenue sur mon API"}

while True:
    try: # To-Do: vars!
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='2YuHHakD7fy6tK88aHm2jd7cuKZMFbjsEBYoYGZtMHtX8BPBsLedxEx3mxvANaNWM8zQdqvPjE7oXZzp37KwhRv7iAd3LNwEVjJj58A27GPHeBPvwyBjWfNQwNvygg79',
        cursor_factory=RealDictCursor) # Makes Python Dict. — pylint: disable=redefined-builtin
        cursor = conn.cursor()
        print("Database connection was sucessful!")
        break
    except Exception as error:
        print("Connecting to the database failed")
        print("Error: ", error)
        time.sleep(2)


my_posts = [{"title": "titre post 1", "content": "contenu du post 1", "id": 1},
            {"title": "Mes plats favoris", "content": "J'aime la pizza", "id": 2}]



@app.get("/posts")
def get_posts():
    posts = cursor.execute(""" SELECT * FROM posts; """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())

    db.add(new_post)
    db.commit()
    # Returning:
    db.refresh(new_post)
    return {"data" : new_post}

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.put("/post/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):

#     cursor.execute(
#         """ UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """,
#                         (post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
    # index = find_index_post(id)

    post_query = db.query(models.Post).filter(models.Post.id == id).update()
    post = post_query.first()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Le post avec l'id:{id} n'existe pas")

    post_query.update({'title' : 'Updated Title', 'content' : 'Udpated Content'},
        synchronize_session = False)

    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_posts[index] = post_dict
    return {'data' : 'test'}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return(post)


# SQLAlchemy ORM test
# @app.get("/sqlalchemy")
# def get_posts(db: Session = Depends(get_db)):
#
#     posts = db.query(models.Post).all()
#     return {"data" : posts}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Le post {id} n'a pas été trouvé.")
    return {"post_detail": f"Voici le post {id}", "post_details": post}


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # trouver l'index dans le tableau qui a le bon ID
    # index = find_index_post(id)
    # cursor.execute(
    #     """ DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # deleted_post =  cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Le post avec l'id: {id} n'existe pas")

    post_query.delete(synchronize_session = False)
    db.commit()

    # my_posts.pop(index)
    # Does not work with HTTP 204:
    # return {"message": f"Le post {id} à bien été supprimé"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)
