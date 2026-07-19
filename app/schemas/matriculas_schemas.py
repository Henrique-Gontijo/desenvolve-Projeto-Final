from pydantic import BaseModel

class CreateMatriculaSchema(BaseModel):
    id_curso: int
    id_aluno: int