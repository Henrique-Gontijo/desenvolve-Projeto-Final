from pydantic import BaseModel

class CreateCursoSchema(BaseModel):
    titulo: str
    descricao: str | None

    model_config = {
        "json_schema_extra": {
            "examples": [
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
            ]
        }
    }


class UpdateCursoSchema(BaseModel):
    titulo: str | None
    descricao: str | None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "titulo": "Python II",
                    "descricao": "Python Intermediário",
                }
            ]
        }
    }

class CreateCursoResponseSchema(BaseModel):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "Successful",
                    "message": "Curso criado com sucesso."
                }
            ]
        }
    }

class UpdateCursoResponseSchema(BaseModel):

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

class GetCursosSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Cursos listados com sucesso.",
                        "data": [
                            {
                                "id": 1,
                                "titulo": "Python",
                                "descricao": "Curso de Introdução ao Python e Lógica de programação.",
                                "deleted": False
                            },
                            {
                                "id": 2,
                                "titulo": "Java",
                                "descricao": "Inserção ao Java e à Programação Orientada a Objetos",
                                "deleted": False
                            },
                            {
                                "id": 3,
                                "titulo": "HTML, CSS e JavaScript",
                                "descricao": "O básico para o desenvolvimeto de Websites",
                                "deleted": False
                            },
                            {
                                "id": 4,
                                "titulo": "Scratch",
                                "descricao": "Introdução à Lógica de Programação com Scratch",
                                "deleted": False
                            }
                        ]
                    }
                ]
            }
        }

class GetCursoByIdSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Curso encontrado com sucesso.",
                        "data": {
                                "id": 1,
                                "titulo": "Python",
                                "descricao": "Curso de Introdução ao Python e Lógica de programação.",
                                "deleted": False
                            }
                    }
                ]
            }
        }

class HardDeleteCursoResponseSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Curso deletado com sucesso."
                    }
                ]
            }
        }

class SoftDeleteCursoResponseSchema(BaseModel):

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

class GetAlunosSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Alunos do curso listados com sucesso.",
                        "data": [
                            {
                                "id": 2,
                                "nome": "Deltrano Costa",
                                "email": "deltranocosta@email.com",
                                "deleted": False
                            }
                        ]
                    }
                ]
            }
        }
        