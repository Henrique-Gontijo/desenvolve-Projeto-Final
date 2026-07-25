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