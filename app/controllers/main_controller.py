from sqlalchemy import select, update
from sqlalchemy.orm import Session

from database.connection import (SessionLocal)
from app.database.models.Alunos import Alunos

session: Session = SessionLocal()

class AlunosController():
    

    def create(nome: str, email: str):

        aluno = Alunos(nome, email)
        session.add(aluno)

        session.commit()


    def get_all():
        response = session.get(Alunos)

        return response
    

    def get_byId(aluno_id: int):
        response = session.get(Alunos, id=aluno_id)

        return response

    def update(aluno_id: int, nome: str, email: str):
        aluno = session.get(Alunos, id=aluno_id)

        new_nome = nome if nome else aluno.nome
        new_email = email if email else aluno.email

        stmt = (
            update(Alunos)
            .where(Alunos.id == aluno_id)
            .values(nome=new_nome, email=new_email)
        )

        session.execute(stmt)

        session.commit()

    def hard_delete(aluno_id):

        aluno = session.get(Alunos, id=aluno_id)
        session.dellete(aluno)

        session.commit()

    def hard_delete(aluno_id):

        stmt = (
            update(Alunos)
            .where(Alunos.id == aluno_id)
            .values(deleted=True)
        )

        session.execute(stmt)

        session.commit()