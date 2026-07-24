from pydantic import BaseModel

class CreateMatriculaSchema(BaseModel):
    id_curso: int
    id_aluno: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id_curso": 1,
                    "id_aluno": 2,
                },
                {
                    "id_curso": 2,
                    "id_aluno": 3,
                },
                {
                    "id_curso": 3,
                    "id_aluno": 1,
                },
                {
                    "id_curso": 4,
                    "id_aluno": 4
                }
            ]   
        }
    }
class CreateMatriculaResponseSchema(BaseModel):

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "status": "Successful",
                    "message": "Matrícula criada com sucesso."
                }
            ]
        }
    }

class GetMatriculasSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "Status": "Successful",
                        "message": "Matrículas listadas com sucesso.",
                        "data": [
                            {
                                "id": 1,
                                "id_curso": 1,
                                "id_aluno": 2,
                                "delted": False
                            },
                            {
                                "id": 2,
                                "id_curso": 2,
                                "id_aluno": 3,
                                "delted": False
                            },
                            {
                                "id": 3,
                                "id_curso": 3,
                                "id_aluno": 1,
                                "delted": False
                            },
                            {
                                "id": 4,
                                "id_curso": 4,
                                "id_aluno": 4,
                                "delted": False
                            }
                        ]
                    }
                ]
            }
        }

class GetMatriculaByIdSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Matrícula encontrada com sucesso.",
                        "data": {
                                    "id": 1,
                                    "id_curso": 1,
                                    "id_aluno": 2,
                                    "delted": False
                                }
                    }
                ]
            }
        }

class HardDeleteMatriculaResponseSchema(BaseModel):

    model_config = {
            "json_schema_extra": {
                "examples": [
                    {
                        "status": "Successful",
                        "message": "Matrícula deletada com sucesso."
                    }
                ]
            }
        }

class SoftDeleteMatriculaResponseSchema(BaseModel):

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