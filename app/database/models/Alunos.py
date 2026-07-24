from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Alunos(Base):
    '''
    Classe de definição da tabela "alunos" no banco de dados.

    Colunas:
        - id (int) --> Chave primária
        - nome (str) --> Nome do aluno (chave única)
        - email (str) --> Email do aluno
        - deleted (bool) --> Indica se o aluno foi deletado ou não (padrão igual a False)

    Construtor:
        - nome (str)
        - email (str)
    '''
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    deleted: Mapped[bool] = mapped_column(default=False)

    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email