from fastapi import APIRouter, HTTPException

from app.database.models.Cursos import Cursos
from app.schemas.cursos_schemas import *
from app.controllers.CursosHandler import CursosHandler
from app.controllers.MatriculasHandler import MatriculasHandler


cursos_router = APIRouter(prefix="/cursos", tags=["cursos"])

@cursos_router.get("/")
async def listar_cursos(status_code=200):
    '''
        # Successful Responses
        
        Retorna a lista de dados dos cursos existentes seguindo o seguinte modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Cursos listados com sucesso.",
            "data": [...]
        }
        ```

        <br>
        Com cada curso seguindo o seguinte formato:

        ```
        {
            "id": 1,
            "titulo": "Programação Orientada a Objetos",
            "descricao": "Tudo sobre o paradigma de POO",
            "deleted": false
        }
        ```

        <br>
        
        Ou talvez:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Nenhum curso encontrado.",
            "data": []
        }
        ```

        <br>
        # Error Reponses

        Em geral, os erros virão no seguinte formato:

        ## Status Code: 500
        ```
        {
            "detail": "Erro desconhecido ao tentar listar os cursos."
        }
        ```
    '''

    response = CursosHandler.get_all()

    if response["status"] == "Error": 
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response
    
@cursos_router.get("/{id_curso}")
async def buscar_curso(id_curso: int, status_code=200):
    '''
        # Successful Response
        
        Retorna os dados do curso de acordo com o modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message": "Curso encontrado com sucesso.",
            "data": {
                "id": 1,
                "titulo": "Programação Orientada a Objetos",
                "descricao": "Tudo sobre o paradigma de POO",
                "deleted": false
            }
        }
        ```

        <br>
        # Error Reponses

        O erro mais comum é de quando se tentar buscar um curso que não existe ou que já foi deleteado

        ## Status Code: 404
        ```
        {
            "detail": "Curso não encontrado."
        }
        ```
    '''

    response = CursosHandler.get_byId(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.post("/cadastro")
async def cadastrar_aluno(schema: CreateCursoSchema, status_code=201):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:
        
        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Curso criado com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 409
        ```
        {
            "detail": "Curso já existente."
        }
        ```
    '''

    response = CursosHandler.create(titulo=schema.titulo, descricao=schema.descricao)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response


@cursos_router.put("/{id_curso}/atualizar_dados")
async def atualizar_dados_curso(id_curso: int, schema: UpdateCursoSchema, status_code=204):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Dados atualizados com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 404
        ```
        {
            "detail": "Curso não encontrado."
        }
        ```

        <br>

        ## Status Code: 409
        ```
        {
            "detail": "Já existe outro curso com esse título."
        }
        ```
    '''

    response = CursosHandler.update(id_curso, titulo=schema.titulo, descricao=schema.descricao)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.delete("/{id_curso}/deletar")
async def deletar_curso(id_curso: int, status_code=204):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Curso deletado com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 404
        ```
        {
            "detail": "Curso não encontrado."
        }
        ```
    '''

    response = CursosHandler.hard_delete(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.delete("/{id_curso}/excluir")
async def excluir_curso(id_curso: int, status_code=204):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Soft delete executado com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 404
        ```
        {
            "detail": "Curso não encontrado."
        }
        ```
    '''

    response = CursosHandler.soft_delete(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@cursos_router.get("/{id_curso}/alunos")
async def listar_alunos_matriculados(id_curso: int, status_code=200):
    '''
        # Successful Responses
        
        Retorna a lista dos alunos matriculados no curso:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Alunos matriculados curso listados com sucesso.",
            "data": [...]
        }
        ```

        <br>
        Com cada aluno seguindo o seguinte formato:

        ```
        {
            "id": 1,
            "nome": "José da Silva",
            "email": "josedasilva@email.com",
            "deleted": false
        }
        ```

        <br>
        
        Ou talvez:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Não há nenhum aluno matriculado neste curso.",
            "data": []
        }
        ```

        <br>
        # Error Reponses

        Em geral, os erros virão no seguinte formato:

        ## Status Code: 404
        ```
        {
            "detail": "Aluno não encontrado."
        }
        ```
    '''

    response = CursosHandler.get_alunos(id_curso)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    
    else:
        return{
            "status": "Successful",
            "message": "Não há nenhum aluno matriculado neste curso.",
            "data": []
        }