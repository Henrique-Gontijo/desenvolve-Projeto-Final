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