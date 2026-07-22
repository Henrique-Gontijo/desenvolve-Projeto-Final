from fastapi import APIRouter, HTTPException

from app.database.models.Cursos import Cursos
from app.schemas.cursos_schemas import CreateCursoSchema, UpdateCursoSchema
from app.controllers.CursosHandler import CursosHandler
from app.controllers.MatriculasHandler import MatriculasHandler


cursos_router = APIRouter(prefix="/cursos", tags=["cursos"])

@cursos_router.get("/")
async def listar_cursos(status_code=200):
    response = CursosHandler.get_all()

    if response["status"] == "Error": 
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    else:
        return {
            "status": "Successful",
            "message": "Nenhum curso encontrado.",
            "data": []
        }
    
@cursos_router.get("/{id_curso}")
async def buscar_curso(id_curso: int, status_code=200):
    response = CursosHandler.get_byId(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.post("/cadastro")
async def cadastrar_aluno(schema: CreateCursoSchema, status_code=201):
    response = CursosHandler.create(titulo=schema.titulo, descricao=schema.descricao)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.put("/{id_curso}")
async def atualizar_dados_curso(id_curso: int, status_code=200):
    response = CursosHandler.get_byId(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response


@cursos_router.put("/{id_curso}/atualizar_dados")
async def atualizar_dados_curso(id_curso: int, schema: UpdateCursoSchema, status_code=204):
    response = CursosHandler.update(id_curso, titulo=schema.titulo, descricao=schema.descricao)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.delete("/{id_curso}/deletar")
async def deletar_curso(id_curso: int, status_code=204):
    response = CursosHandler.hard_delete(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.delete("/{id_curso}/excluir")
async def excluir_curso(id_curso: int, status_code=204):
    response = CursosHandler.soft_delete(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.get("/{id_curso}/alunos")
async def listar_alunos_matriculados(id_curso: int, status_code=200):
    response = CursosHandler.get_alunos(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    
    else:
        return{
            "status": "Successful",
            "message": "Não há nenhum aluno cadastrado neste curso.",
            "data": []
        }