from fastapi import FastAPI

from app.database.connection import (Base, engine)
from app.controllers.main_controller import AlunosController



app = FastAPI()

Base.metadata.create_all(bind=engine)

AlunosController.create("John", "jao@mail.com")

'''
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None ):
    return {"item_id": item_id, "q": q}

'''