from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange



app = FastAPI()

class Post(BaseModel):
    title: str 
    content: str
    published: bool = True 
    rating: Optional[int] = None 

my_posts = [{"title": "titre post 1", "content": "contenu du post 1", "id": 1}, {"title": "Mes plats favoris", "content": "J'aime la pizza", "id": 2}]

@app.get("/") 
def root():
    return {"message":"Bienvenue sur mon API"}

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return{"data": post_dict}

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return(post)

@app.get("/posts/{id}")
def get_specific_post(id: int):
    post = find_post(id)
    print(post)
    return {"post_detail" : f"Voici le post {id}", "post_details" : post}


# @app.get("/posts/{id}")
# def get_specific_post(id: str):

