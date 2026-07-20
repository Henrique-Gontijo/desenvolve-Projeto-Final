from fastapi import APIRouter, HTTPException

from app.database.models.Cursos import Cursos
from app.schemas.cursos_schemas import CreateCursoSchema, UpdateCursoSchema
from app.controllers.CursosHandler import CursosHandler
from app.controllers.MatriculasHandler import MatriculasHandler


cursos_router = APIRouter(prefix="/cursos", tags=["cursos"])

@cursos_router.get("/")
async def listar_cursos(status_code=200):
    cursos = CursosHandler.get_all()

    if cursos and len(cursos) > 0:
        return {
            "message": "Cursos listados com sucesso",
            "cursos": cursos
        }
    
    else:
        return {
            "message": "Nenhum curso encontrado.",
            "cursos": []
        }

@cursos_router.post("/cadastro")
async def cadastrar_aluno(schema: CreateCursoSchema, status_code=201):
    CursosHandler.create(titulo=schema.titulo, descricao=schema.descricao)

    return {"message": "Curso cadastrado com sucesso!"}

@cursos_router.put("/{id_curso}")
async def atualizar_dados_curso(id_curso: int, status_code=200):
    curso = CursosHandler.get_byId(id_curso)

    if curso and (not curso == {}):
        return {
            "message": "Curso encontrado com sucesso!",
            "curso": curso
        }
    
    else:
        return {
            "message": "Curso não encontrado ou inexistente.",
            "curso": {}
        }
    
    #TODO colocar erro de curso não encontrado


@cursos_router.put("/{id_curso}/atualizar_dados")
async def atualizar_dados_curso(id_curso: int, schema: UpdateCursoSchema, status_code=200):
    CursosHandler.update(id_curso, titulo=schema.titulo, descricao=schema.descricao)

@cursos_router.delete("/{id_curso}/deletar")
async def deletar_curso(id_curso: int, status_code=400):
    CursosHandler.hard_delete(id_curso)

@cursos_router.post("/{id_curso}/deletar")
async def excluir_curso(id_curso: int, status_code=400):
    CursosHandler.soft_delete(id_curso)

@cursos_router.get("/{id_curso}/alunos")
async def listar_alunos_matriculados(id_curso: int, status_code=200):
    alunos = CursosHandler.get_alunos(id_curso)

    if alunos and len(alunos) > 0:
        return {
            "message": "Alunos matriculados no curso listados com sucesso",
            "alunos_matriculados": alunos
        }
    
    else:
        return {
            "message": "Nenhum aluno matriculado no curso encontrado.",
            "alunos_matriculados": []
        }

@cursos_router.get("/{id_curso}/matricular_aluno")
async def matricular_aluno(id_curso: int, id_aluno: int):
    MatriculasHandler.create(id_curso, id_aluno)