from fastapi import APIRouter, HTTPException

from app.database.models.Alunos import Alunos
from app.schemas.alunos_schemas import CreateAlunoSchema, UpdateAlunoSchema
from app.controllers.AlunosHandler import AlunosHandler


alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/")
async def listar_aluno(status_code=200):
    response = AlunosHandler.get_all()


    if response["status"] == "Error": 
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    else:
        return {
            "status": "Successful",
            "message": "Nenhum aluno encontrado.",
            "data": []
        }
    
@alunos_router.get("/{id_aluno}")
async def buscar_aluno(id_aluno: int, status_code=200):
    response = AlunosHandler.get_byId(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.post("/cadastro")
async def cadastrar_aluno(schema: CreateAlunoSchema, status_code=201):
    response = AlunosHandler.create(nome=schema.nome, email=schema.email)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.put("/{id_aluno}/atualizar_dados")
async def atualizar_dados_aluno(id_aluno: int, schema: UpdateAlunoSchema, status_code=204):
    response = AlunosHandler.update(id_aluno, nome=schema.nome, email=schema.email)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.delete("/{id_aluno}/deletar")
async def deletar_aluno(id_aluno: int, status_code=204):
    response = AlunosHandler.hard_delete(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.delete("/{id_aluno}/excluir")
async def excluir_aluno(id_aluno: int, status_code=204):
    response = AlunosHandler.soft_delete(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.get("/{id_aluno}/cursos")
async def listar_cursos_aluno(id_aluno: int, status_code=200):
    response = AlunosHandler.get_cursos(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    
    else:
        return{
            "status": "Successful",
            "message": "O aluno não está cadastrado em nenhum curso.",
            "data": []
        }