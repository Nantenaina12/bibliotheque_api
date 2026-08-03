from fastapi import FastAPI

from app.database import Base, engine

from app.models.livre import Livre
from app.models.etudiant import Etudiant
from app.models.emprunt import Emprunt

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API Bibliothèque"}