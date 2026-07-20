from fastapi import FastAPI

from app.database.connection import (Base, engine)
from app.controllers.AlunosHandler import AlunosHandler as AlunosHndl
from app.controllers.CursosHandler import CursosHandler as CursosHndl
from app.controllers.MatriculasHandler import MatriculasHandler as MatriculasHndl
from app.routes.alunos import alunos_router



app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(alunos_router)

alunos = AlunosHndl.get_all()
aluno = AlunosHndl.get_byId(1)

cursos = CursosHndl.get_all()
curso = CursosHndl.get_byId(1)

matriculas = MatriculasHndl.get_all()
matricula = MatriculasHndl.get_byId(1)


@app.get("/")
def read_root():
    '''
    return {
        "Hello": "World",
        "alunos": {
            "listagem": alunos,
            "top1": aluno
        },
        "cursos": {
            "listagem": cursos,
            "top1": curso
        },
        "matriculas": {
            "listagem": matriculas,
            "top1": matricula
        }
    }
    '''
    dados = AlunosHndl.get_cursos(1)
    print(dados)

    return {
        "Dados": 12345
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None ):
    return {"item_id": item_id, "q": q}
