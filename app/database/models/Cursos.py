from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Cursos(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(180), nullable=False)
    descricao: Mapped[Optional[str]]
    deleted: Mapped[bool] = mapped_column(default=False)