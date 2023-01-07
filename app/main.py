from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post,user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# Automatic documentation (Swagger UI):
# http://127.0.0.1:8000/docs/
# http://127.0.0.1:8000/redoc/

# deprecated w/ Alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur mon API"}
