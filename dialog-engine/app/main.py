from fastapi import FastAPI
from . import models
from .database import engine
from .routes import user, whatsapp

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(whatsapp.router)
