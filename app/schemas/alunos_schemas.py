from typing import Optional
from pydantic import BaseModel

class CreateAlunoSchema(BaseModel):
    nome: str
    email: str

    model_config = {
        "json_schema_extra": {
            "examples": [
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
            ]
        }
    }


class UpdateAlunoSchema(BaseModel):
    nome: Optional[str]
    email: Optional[str]

    model_config = {
            "json_schema_extra": {
                "examples": [
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
                ]
            }
        }

class CreateAlunoResponseSchema(BaseModel):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "Successful",
                    "message": "Aluno criado com sucesso."
                }
            ]
        }
    }

class UpdateAlunoResponseSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Dados atualizados com sucesso."
                    }
                ]
            }
        }

class GetAlunosSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "Status": "Successful",
                        "message": "Alunos listados com sucesso.",
                        "data": [
                            {
                                "id": 1,
                                "nome": "Fulano da Silva",
                                "email": "fulanosilva@email.com",
                                "deleted": False
                            },
                            {
                                "id": 2,
                                "nome": "Deltrano Costa",
                                "email": "deltranocosta@email.com",
                                "deleted": False
                            },
                            {
                                "id": 3,
                                "nome": "Sicrano Freitas",
                                "email": "sicranofreitas@email.com",
                                "deleted": False
                            },
                            {
                                "id": 4,
                                "nome": "Beltrano Mendonça",
                                "email": "beltranomendonca@email.com",
                                "deleted": False
                            }
                        ]
                    }
                ]
            }
        }

class GetAlunoByIdSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Aluno encontrado com sucesso.",
                        "data": {
                                "id": 1,
                                "nome": "Fulano da Silva",
                                "email": "fulanosilva@email.com",
                                "deleted": False
                            }
                    }
                ]
            }
        }

class HardDeleteAlunoResponseSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Aluno deletado com sucesso."
                    }
                ]
            }
        }

class SoftDeleteAlunoResponseSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Soft Delete executado com sucesso."
                    }
                ]
            }
        }

class GetCursosSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Cursos do aluno listados com sucesso.",
                        "data": [
                            {
                                "id": 3,
                                "titulo": "HTML, CSS e JavaScript",
                                "descricao": "O básico para o desenvolvimeto de Websites",
                                "deleted": False
                            }
                        ]
                    }
                ]
            }
        }