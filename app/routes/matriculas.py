from fastapi import APIRouter, HTTPException

from app.schemas.matriculas_schemas import *
from app.controllers.MatriculasHandler import MatriculasHandler


matriculas_router = APIRouter(prefix="/matriculas", tags=["matriculas"])

@matriculas_router.get("/")
async def listar_matriculas(status_code=200):
    '''
        # Successful Responses
        
        Retorna a lista de matrículas existentes seguindo o seguinte modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Matrículas listadas com sucesso.",
            "data": [...]
        }
        ```

        <br>
        Com cada matrícula seguindo o seguinte formato:

        ```
        {
            "id": 1,
            "id_curso": "1",
            "id_aluno": "1",
            "deleted": false
        }
        ```

        <br>
        
        Ou talvez:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Nenhuma matrícula encontrada.",
            "data": []
        }
        ```

        <br>
        # Error Reponses

        Em geral, os erros virão no seguinte formato:

        ## Status Code: 500
        ```
        {
            "detail": "Erro desconhecido ao tentar listar as matrículas."
        }
        ```
    '''

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
    '''
        # Successful Response
        
        Retorna a matrícula de acordo com o modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message": "Matrícula encontrada com sucesso.",
            "data": {
                "id": 1,
                "id_curso": "1",
                "id_aluno": "1",
                "deleted": false
            }
        }
        ```

        <br>
        # Error Reponses

        O erro mais comum é de quando se tentar buscar um aluno que não existe ou que já foi deleteado

        ## Status Code: 404
        ```
        {
            "detail": "Matrícula não encontrada."
        }
        ```
    '''

    response = MatriculasHandler.get_byId(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.post("/cadastro")
async def cadastrar_matricula(schema: CreateMatriculaSchema, status_code=201):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Matrícula criada com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 409
        ```
        {
            "detail": "Matrícula já existente."
        }
        ```
    '''

    response = MatriculasHandler.create(id_curso=schema.id_curso, id_aluno=schema.id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.delete("/{id_matricula}/deletar")
async def deletar_matricula(id_matricula: int, status_code=204):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Matrícula deletada com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 404
        ```
        {
            "detail": "Matrícula não encontrada."
        }
        ```
    '''

    response = MatriculasHandler.hard_delete(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@matriculas_router.delete("/{id_matricula}/excluir")
async def excluir_matricula(id_matricula: int, status_code=204):
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
            "detail": "Matrícula não encontrada."
        }
        ```
    '''

    response = MatriculasHandler.soft_delete(id_matricula)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response