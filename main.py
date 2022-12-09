from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Classe qui contruit le poste. 
# N'autoriser qu'un seul type de données, des lignes de caractères (les int peuvent être transcrits en str)
class Post(BaseModel):
    title: str # Si aucune donnée n'est présente, retourne une erreur (pour les strings)
    content: str
    published: bool = True # Si l'utilisateur ne publie pas, vrai par défaut
    rating: Optional[int] = None # Si l'utilisateur met un string contenant un nombre, la string sera transformée en nombre

# Un décorateur est une fonction qui prend en paramètre une fonction et qui retourne une fonction.
# L’intérêt d’un décorateur est qu’il permet de transformer le comportement de la fonction passée en paramètre pour exécuter des traitements supplémentaires avant ou après les traitement normal de la fonction passée en paramètre.
# Ici, @app (décorateur) faisant referrence à "app" et appel la méthode HTTP GET avec ".get".
# ("/") = URL path
# ie. : @app.post("/posts/vote")
@app.get("/") # Path operation: "décorateur" qui fera fonctionner le code comme une API
# Fonction
# async def root():
def root(): # Pour indiquer à l'interpréteur que vous voulez créer une fonction , on utilise le mot clé def suivi d'un nom puis de parenthèses et ensuite d'un double point.
    # Retourne un dictionnaire Python qui sera transformé en JSON.
    return {"message":"Bienvenue sur mon API"}

# À chaque fois que le code est modifier il faudrat redémarrer le serveur (uvicorn).
# Avec le flag --reload, le serveur se redémarre automatiquement.


# Enregistrer (dans la mémoire) les post dans un array (tableau), et dictionnaire
my_posts = [{"title": "titre post 1", "content": "contenu du post 1", "id": 1}, {"title": "Mes plats favoris", "content": "J'aime la pizza", "id": 2}]

@app.get("/data")
def get_posts():
    return{"data": my_posts}

@app.post("/posts") # Always use plural standard convention: ie.: POST request will be /posts
def post(new_post: Post):
    print(new_post.published)
    # Each pydantic model has a method ".dict"
    # So if I need to convert a pydantic model to dictionnary :
    # print(new_post.dict) # Retourne alors un dictionnaire des propriétés de ce model ("la requête").
    return{"data": "new_post"}

# CRUD : Create (POST), Read (GET), Update (PUT/PATCH), DELETE
# Read exemple: GET to /posts/:id (@app.put("/posts/{id}")). ":id" for specific post.
# Update exemple: @app.put("/posts/{id}")

