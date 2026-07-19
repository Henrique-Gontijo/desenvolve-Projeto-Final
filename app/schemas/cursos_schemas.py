from pydantic import BaseModel

class CreateCursoSchema(BaseModel):
    titulo: str
    descricao: str | None


class UpadateCursoSchema:
    titulo: str | None
    descricao: str | None