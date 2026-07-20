from fastapi import APIRouter, HTTPException

from app.database.models.Alunos import Alunos
from app.schemas.alunos_schemas import CreateAlunoSchema, UpadateAlunoSchema
from app.controllers.AlunosHandler import AlunosHandler


alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def listar_aluno(status_code=200):
    alunos = AlunosHandler.get_all()

    if alunos and len(alunos) > 0:
        return {
            "message": "Alunos listados com sucesso",
            "alunos": alunos
        }
    
    else:
        return {
            "message": "Nenhum aluno encontrado.",
            "alunos": []
        }

@alunos_router.post("/cadastro")
async def cadastrar_aluno(schema: CreateAlunoSchema, status_code=201):
    AlunosHandler.create(nome=schema.nome, email=schema.email)

    return {"message": "Aluno cadastrado com sucesso!"}

@alunos_router.get("/{id_aluno}")
async def buscar_aluno(id_aluno: int, status_code=200):
    aluno = AlunosHandler.get_byId(id_aluno)

    if aluno and (not aluno == {}):
        return {
            "message": "Aluno encontrado com sucesso!",
            "aluno": aluno
        }
    
    else:
        return {
            "message": "Aluno não encontrado ou inexistente.",
            "aluno": {}
        }
    
    #TODO colocar erro de aluno não encontrado


@alunos_router.put("/{id_aluno}/atualizar_dados")
async def atualizar_dados_aluno(id_aluno: int, schema: UpadateAlunoSchema, status_code=200):
    AlunosHandler.update(id_aluno, nome=schema.nome, email=schema.email)

@alunos_router.delete("/{id_aluno}/deletar")
async def deletar_aluno(id_aluno: int, status_code=400):
    AlunosHandler.hard_delete(id_aluno)

@alunos_router.put("/{id_aluno}/deletar")
async def ecluir_aluno(id_aluno: int, status_code=400):
    AlunosHandler.soft_delete(id_aluno)

@alunos_router.get("/{id_aluno}/cursos")
async def listar_cursos_aluno(id_aluno: int, status_code=200):
    cursos = AlunosHandler.get_cursos(id_aluno)

    if cursos:
        return {
            "message": "Cursos do aluno listados com sucesso!",
            "cursos": cursos
        }
    
    else:
        return {
            "message": "Nenhum curso do aluno encontrado.",
            "cursos": []
        }