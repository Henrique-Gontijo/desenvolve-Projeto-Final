from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Cursos(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(180), nullable=False, unique=True)
    descricao: Mapped[Optional[str]]
    deleted: Mapped[bool] = mapped_column(default=False)

    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao