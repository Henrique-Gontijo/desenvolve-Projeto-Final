from pydantic import BaseModel

class CreateAlunoSchema(BaseModel):
    nome: str
    email: str


class UpadateAlunoSchema:
    nome: str | None
    email: str | None