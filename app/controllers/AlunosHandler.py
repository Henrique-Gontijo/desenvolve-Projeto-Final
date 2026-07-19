from sqlalchemy import update, select
from sqlalchemy.orm import Session

from app.database.connection import (SessionLocal)
from app.database.models.Alunos import Alunos
from app.database.models.Cursos import Cursos
from app.database.models.Matriculas import Matriculas

session: Session = SessionLocal()

class AlunosHandler():

#TODO ---> O aluno em questão já existe?

    def create( nome: str, email: str):
        aluno = Alunos(nome, email)
        session.begin()
        session.add(aluno)

        session.commit()

#TODO --> Os alunos marcados como "deleted" devem ser listados?

    def get_all():
        session.begin()
        response = session.query(Alunos).all()
        session.close()

        return response

#TODO ---> O que acontece se nenhum aluno for encontrado? (get_byId, update, hard_delete e soft_delete)

    def get_byId(id_aluno: int):
        session.begin()
        response = session.get(Alunos, id_aluno)
        session.close()

        return response

    def update(id_aluno: int, nome: str = None, email: str = None):
        session.begin()
        aluno = session.get(Alunos, id_aluno)

        new_nome = nome if nome and nome != "" else aluno.nome
        new_email = email if email and email != "" else aluno.email

        stmt = (
            update(Alunos)
            .where(Alunos.id_aluno == id_aluno)
            .values(nome=new_nome, email=new_email)
        )

        session.execute(stmt)
        session.commit()
        session.close()

#TODO ---> As matrículas de alunos deletados devem ser apgadas também, certo?

    def hard_delete(id_aluno):
        session.begin()
        aluno = session.get(Alunos, id_aluno)
        session.delete(aluno)
        session.commit()
        session.close()

    def soft_delete(id_aluno):

        stmt = (
            update(Alunos)
            .where(Alunos.id_aluno == id_aluno)
            .values(deleted=True)
        )

        session.begin()
        session.execute(stmt)
        session.commit()
        session.close()

    def get_cursos(id_aluno):

        ids_cursos = session.query(Matriculas.id_curso).where(Matriculas.id_aluno == id_aluno)
        cursos = session.query(Cursos).where(Cursos.id in ids_cursos)

        return cursos