from fastapi import APIRouter, HTTPException

from app.database.models.Matriculas import Matriculas
from app.schemas.matriculas_schemas import CreateMatriculaSchema
from app.controllers.MatriculasHandler import MatriculasHandler


matriculas_router = APIRouter(prefix="/matriculas", tags=["matriculas"])

@matriculas_router.get("/")
async def listar_matriculas(status_code=200):
    response = MatriculasHandler.get_all()

    if response["status"] == "Error": 
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    else:
        return {
            "status": "Successful",
            "message": "Nenhuma matrícula encontrada.",
            "data": []
        }
    
@matriculas_router.get("/{id_matricula}")
async def buscar_matricula(id_matricula: int, status_code=200):
    response = MatriculasHandler.get_byId(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.post("/cadastro")
async def cadastrar_matricula(schema: CreateMatriculaSchema, status_code=201):
    response = MatriculasHandler.create(id_curso=schema.id_curso, id_aluno=schema.id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.delete("/{id_matricula}/deletar")
async def deletar_matricula(id_matricula: int, status_code=204):
    response = MatriculasHandler.hard_delete(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.delete("/{id_matricula}/excluir")
async def excluir_matricula(id_matricula: int, status_code=204):
    response = MatriculasHandler.soft_delete(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response