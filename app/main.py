from fastapi import FastAPI

from app.database.connection import (Base, engine, SessionLocal)
from app.controllers.AlunosHandler import AlunosHandler as AlunosHndl
from app.controllers.CursosHandler import CursosHandler as CursosHndl
from app.controllers.MatriculasHandler import MatriculasHandler as MatriculasHndl
from app.database.models.Alunos import Alunos
from app.database.models.Cursos import Cursos
from app.database.models.Matriculas import Matriculas
from app.routes.alunos import alunos_router
from app.routes.cursos import cursos_router
from app.routes.matriculas import matriculas_router


app = FastAPI()

Base.metadata.create_all(bind=engine)
app.include_router(alunos_router)
app.include_router(cursos_router)
app.include_router(matriculas_router)


'''
dados_injecao = {
    "alunos": [
        {
            "nome": "Fulano da Silva",
            "email": "fulanosilva@email.com"
        },
        {
            "nome": "Deltrano Costa",
            "email": "deltranocosta@email.com"
        },
        {
            "nome": "Sicrano Freitas",
            "email": "sicranofreitas@email.com"
        },
        {
            "nome": "Beltrano Mendonça",
            "email": "beltranomendonca@email.com"
        }
    ],
    "cursos": [
        {
            "titulo": "Python",
            "descricao": "Curso de Introdução ao Python e Lógica de programação."
        },
        {
            "titulo": "Java",
            "descricao": "Inserção ao Java e à Programação Orientada a Objetos"
        },
        {
            "titulo": "HTML, CSS e JavaScript",
            "descricao": "O básico para o desenvolvimeto de Websites"
        },
        {
            "titulo": "Scratch",
            "descricao": "Introdução à Lógica de Programação com Scratch"
        }
    ],
    "matriculas": [
        {
            "id_curso": 1,
            "id_aluno": 2,
        },
        {
            "id_curso": 2,
            "id_aluno": 3,
        },
        {
            "id_curso": 3,
            "id_aluno": 1,
        },
        {
            "id_curso": 4,
            "id_aluno": 4
        }
    ]
}

for aluno in dados_injecao["alunos"]:
    AlunosHndl.create(nome=aluno["nome"], email=aluno["email"])

for curso in dados_injecao["cursos"]:
    CursosHndl.create(titulo=curso["titulo"], descricao=curso["descricao"])

for matricula in dados_injecao["matriculas"]:
    MatriculasHndl.create(id_curso=matricula["id_curso"], id_aluno=matricula["id_aluno"])

AlunosHndl.soft_delete(4)
CursosHndl.soft_delete(4)
MatriculasHndl.soft_delete(4)
'''

session = SessionLocal()
session.begin()

data = session.query(Matriculas).where(Matriculas.id_aluno == 5).where(Matriculas.deleted == False).all()

#cursos = AlunosHndl.get_cursos(1)
#alunos = CursosHndl.get_alunos(1)


@app.get("/")
def read_root():
    
    return {
        "data": data
    }
    
    #return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None ):
    return {"item_id": item_id, "q": q}
