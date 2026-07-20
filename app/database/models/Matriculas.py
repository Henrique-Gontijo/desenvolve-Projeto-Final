from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Matriculas(Base):
    __tablename__ = "matriculas"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    id_curso: Mapped[int] = mapped_column(ForeignKey("cursos.id"), nullable=False)
    id_aluno: Mapped[int] = mapped_column(ForeignKey("alunos.id"), nullable=False)
    deleted: Mapped[bool] = mapped_column(default=False)

    def __init__(self, id_curso, id_aluno):
        self.id_curso = id_curso
        self.id_aluno = id_aluno