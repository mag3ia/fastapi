from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Classe qui contruit le poste. 
# N'autoriser qu'un seul type de données, des lignes de caractères (les int peuvent être transcrits en str)
# Si aucune donnée n'est présente, retourne une erreur
class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Si l'utilisateur ne publie pas, vrai par défaut
    rating: Optional[int] = None # Si l'utilisateur met un string contenant un nombre, la string sera transformée en nombre

# Path operation: "décorateur" qui fera fonctionner le code comme une API:
# @app (décorateur) faisant referrence à "app" et appel la méthode HTTP GET.
# ("/") = URL path
# ie. : @app.post("/posts/vote")
@app.get("/")
# Fonction
# async def root():
def root():
    # Retourne un dictionnaire Python qui sera transformé en JSON.
    return {"message":"Bienvenue sur mon API"}

# À chaque fois que le code est modifier il faudrat redémarrer le serveur (uvicorn).
# Avec le flag --reload, le serveur se redémarre automatiquement.

@app.get("/data")
def get_posts():
    return{"data":"Les données"}

@app.post("/post")
def post(new_post: Post):
    print(new_post.published)
    # Each pydantic model has a method ".dict"
    # So if I need to convert a pydantic model to dictionnary :
    # print(new_post.dict) # Retourne alors un dictionnaire des propriétés de ce model ("la requête").
    return{"data": "new_post"}

# CRUD : Create (POST), Read (GET), Update (PUT/PATCH), DELETE
# Update exemple: @app.get("/posts/{id}")
# Always use plural standard convention:
# ie.: POST request will be /posts

