from pydantic import BaseModel

class CreateAlunoSchema(BaseModel):
    nome: str
    email: str


class UpdateAlunoSchema(BaseModel):
    nome: str | None
    email: str | None