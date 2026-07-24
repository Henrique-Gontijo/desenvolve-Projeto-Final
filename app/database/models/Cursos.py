from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Cursos(Base):
    '''
    Classe de definição da tabela "cursos" no banco de dados.

    Colunas:
        - id (int) --> Chave primária
        - titulo (str) --> Título do curso (chave única)
        - descricao (Optional[str]) --> Descrição do curso
        - deleted (bool) --> Indica se o curso foi deletado ou não (padrão igual a False)

    Construtor:
        - titulo (str)
        - descricao (Optional[str])
    '''

    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(180), nullable=False, unique=True)
    descricao: Mapped[Optional[str]]
    deleted: Mapped[bool] = mapped_column(default=False)

    def __init__(self, titulo: str, descricao: Optional[str] = None):
        self.titulo = titulo
        self.descricao = descricao