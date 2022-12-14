from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


# Automatic documentation :
# http://127.0.0.1:8000/docs/
# http://127.0.0.1:8000/redoc/

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
def create_posts(post: Post):
    # Le code suivant n'est pas bon car vulnérable à la SQLInjection :
    # cursor.execute(f" INSERT INTO posts (title, content, published) VALUES({post.title}, {post.content}, {post.published}")
    # On utilisera la méthode suviante pour s'en prévenir:
    cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    new_post = cursor.fetchone()

    # Push to PSQL DB:
    conn.commit()
    return {"data": new_post}
    # return {"data" : "Post créé."}

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.put("/post/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Le post avec l'id:{id} n'existe pas")

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data' : post_dict}

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts) - 1]
    return (post)


@app.get("/posts/{id}")
def get_specific_post(id: str):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Le post {id} n'a pas été trouvé.")
    return {"post_detail": f"Voici le post {id}", "post_details": post}


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # trouver l'index dans le tableau qui a le bon ID
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Le post avec l'id:{id} n'existe pas")

    my_posts.pop(index)
    # Does not work with HTTP 204:
    # return {"message": f"Le post {id} à bien été supprimé"}
    return Response(status_code=status.HTTP_204_NO_CONTENT)

