from fastapi import FastAPI, Response, status, HTTPException
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


my_posts = [{"title": "titre post 1", "content": "contenu du post 1", "id": 1},
            {"title": "Mes plats favoris", "content": "J'aime la pizza", "id": 2}]


@app.get("/")
def root():
    return {"message": "Bienvenue sur mon API"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


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
def get_specific_post(id: int, response: Response):
    post = find_post(id)
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

