from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

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
def post(payload: dict = Body(...)):
    print(payload)
    return{"new_post": f"title:{payload['title']} content: {payload['content']}"}
