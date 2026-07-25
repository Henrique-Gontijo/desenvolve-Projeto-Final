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