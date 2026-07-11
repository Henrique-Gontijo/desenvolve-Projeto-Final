from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class CursosAlunos(Base):
    __tablename__ = "cursos_alunos"

    id_curso: Mapped[int] = mapped_column(ForeignKey("cursos.id"), nullable=False)
    id_aluno: Mapped[int] = mapped_column(ForeignKey("alunos.id"), nullable=False)
    deleted: Mapped[bool] = mapped_column(default=False)