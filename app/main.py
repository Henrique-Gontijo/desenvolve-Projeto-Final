from fastapi import FastAPI

from app.database.connection import (Base, engine)
from app.controllers.AlunosHandler import AlunosHandler as AlunosHndl



app = FastAPI()

Base.metadata.create_all(bind=engine)

AlunosHndl.create(nome="Carmélia", email="carma@mail.com")
alunos = AlunosHndl.get_all()
aluno = AlunosHndl.get_byId(1)
#AlunosHndl.update(2, "Wellington", "well@email.com")
#AlunosHndl.hard_delete(3)
#AlunosHndl.soft_delete(1)



@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "alunos": alunos,
        "aluno_top": aluno
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None ):
    return {"item_id": item_id, "q": q}
