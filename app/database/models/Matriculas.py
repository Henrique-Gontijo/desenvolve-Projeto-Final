from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Matriculas(Base):
    '''
    Classe de definição da tabela de relacionamento "matriculas" no banco de dados.

    Colunas:
        - id (int) --> Chave primária
        - id_curso (int) --> ID do curso (chave estrangeira)
        - id_aluno (int) --> ID do aluno (chave estrangeira)
        - deleted (bool) --> Indica se a matrícula foi deletada ou não (padrão igual a False)

    Construtor:
        - id_curso (int)
        - id_aluno (int)
    '''

    __tablename__ = "matriculas"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("cursos.id"), nullable=False)
    id_aluno: Mapped[int] = mapped_column(ForeignKey("alunos.id"), nullable=False)
    deleted: Mapped[bool] = mapped_column(default=False)

    def __init__(self, id_curso: int, id_aluno: int):
        self.id_curso = id_curso
        self.id_aluno = id_aluno

    def to_dict(self):
        return {
            "id": self.id,
            "id_curso": self.id_curso,
            "id_aluno": self.id_aluno,
            "delted": self.deleted
        }