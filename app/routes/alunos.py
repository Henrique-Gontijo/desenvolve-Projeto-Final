from fastapi import APIRouter, HTTPException

from app.database.models.Alunos import Alunos
from app.schemas.alunos_schemas import *
from app.controllers.AlunosHandler import AlunosHandler


alunos_router = APIRouter(prefix="/alunos", tags=["alunos"])

@alunos_router.get("/", response_model=GetAlunosSchema)
async def listar_alunos(status_code=200):
    '''
        # Successful Responses
        
        Retorna a lista de dados dos alunos existentes seguindo o seguinte modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Alunos listados com sucesso.",
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
            "message: "Nenhum aluno encontrado.",
            "data": []
        }
        ```

        <br>
        # Error Reponses

        Em geral, os erros virão no seguinte formato:

        ## Status Code: 500
        ```
        {
            "detail": "Erro desconhecido ao tentar listar os alunos."
        }
        ```
    '''
    
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
    
@alunos_router.get("/{id_aluno}", response_model=GetAlunoByIdSchema)
async def buscar_aluno(id_aluno: int, status_code=200):
    '''
        # Successful Response
        
        Retorna os dados do aluno de acordo com o modelo:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message": "Aluno encontrado com sucesso.",
            "data": {
                "id": 1,
                "nome": "José da Silva",
                "email": "josedasilva@email.com",
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
            "detail": "Aluno não encontrado."
        }
        ```
    '''

    response = AlunosHandler.get_byId(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.post("/cadastro", response_model=CreateAlunoResponseSchema)
async def cadastrar_aluno(schema: CreateAlunoSchema, status_code=201):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Aluno criado com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 409
        ```
        {
            "detail": "Aluno já existente."
        }
        ```
    '''

    response = AlunosHandler.create(nome=schema.nome, email=schema.email)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.put("/{id_aluno}/atualizar_dados", response_model=UpdateAlunoResponseSchema)
async def atualizar_dados_aluno(id_aluno: int, schema: UpdateAlunoSchema, status_code=204):
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
            "detail": "Aluno não encontrado."
        }
        ```

        <br>

        ## Status Code: 409
        ```
        {
            "detail": "Já existe outro aluno com esse nome."
        }
        ```
    '''

    response = AlunosHandler.update(id_aluno, nome=schema.nome, email=schema.email)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.delete("/{id_aluno}/deletar")
async def deletar_aluno(id_aluno: int, status_code=204, reponse_model=HardDeleteAlunoResponseSchema):
    '''
        # Successful Response
        
        Retorna apenas o informe de que a operação foi realizada com suceeso:

        ```
        ## Status Code: 201
        {
            "status": "Successful",
            "message": "Aluno deletado com sucesso.",
        }
        ```

        <br>
        # Error Reponses

        ## Status Code: 404
        ```
        {
            "detail": "Aluno não encontrado."
        }
        ```
    '''
    response = AlunosHandler.hard_delete(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.delete("/{id_aluno}/excluir")
async def excluir_aluno(id_aluno: int, status_code=204, response_model=SoftDeleteAlunoResponseSchema):
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
            "detail": "Aluno não encontrado."
        }
        ```
    '''

    response = AlunosHandler.soft_delete(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])

    return response

@alunos_router.get("/{id_aluno}/cursos")
async def listar_cursos_aluno(id_aluno: int, status_code=200, response_model=GetCursosSchema):
    '''
        # Successful Responses
        
        Retorna a lista dos cursos em que o aluno está matriculado:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "Cursos do aluno listados com sucesso.",
            "data": [...]
        }
        ```

        <br>
        Com cada curso seguindo o seguinte formato:

        ```
        {
            "id": 1,
            "titulo": "Programação Orientada a Objetos",
            "descricao": "Tudo sobre o paradigma de POO.",
            "deleted": false
        }
        ```

        <br>
        
        Ou talvez:

        ## Status Code: 200
        ```
        {
            "status": "Successful",
            "message: "O aluno não está matriculado em nenhum curso.",
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

    response = AlunosHandler.get_cursos(id_aluno)

    if response["status"] == "Error":
        raise HTTPException(status_code=response["status_code"], detail=response["message"])
    
    if len(response["data"]) > 0:
        return response
    
    else:
        return{
            "status": "Successful",
            "message": "O aluno não está matriculado em nenhum curso.",
            "data": []
        }