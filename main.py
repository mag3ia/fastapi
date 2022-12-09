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
    rating: Optional[int] = None

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
    return{"data": "new_post"}
