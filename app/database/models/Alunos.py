from sqlalchemy import String
from sqlalchemy.orm import (Mapped, mapped_column)

from app.database.connection import Base

class Alunos(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    deleted: Mapped[bool] = mapped_column(default=False)