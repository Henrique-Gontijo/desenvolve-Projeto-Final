from sqlalchemy import update
from sqlalchemy.orm import Session

from app.database.connection import (SessionLocal)
from app.database.models.Cursos import Cursos
from app.database.models.Alunos import Alunos
from app.database.models.Matriculas import Matriculas

session: Session = SessionLocal()

class CursosHandler():

#TODO ---> O curso em questão já existe?

    def create( titulo: str, descricao: str = None):
        aluno = Cursos(titulo, descricao)
        session.begin()
        session.add(aluno)

        session.commit()
        session.close()

#TODO --> Os cursos marcados como "deleted" devem ser listados?

    def get_all():
        session.begin()
        response = session.query(Cursos).all()
        session.close()

        return response
    
#TODO ---> O que acontece se nenhum curso for encontrado? (get_byId, update, hard_delete e soft_delete)

    def get_byId(id: int):
        session.begin()
        response = session.get(Cursos, id)
        session.close()

        return response

    def update(id: int, titulo: str = None, descricao: str = None):
        session.begin()
        curso = session.get(Cursos, id)

        new_titulo = titulo if titulo and titulo != "" else curso.titulo
        new_descricao = descricao if descricao and descricao != "" else curso.descricao

        stmt = (
            update(Cursos)
            .where(Cursos.id == id)
            .values(titulo=new_titulo, descricao=new_descricao)
        )

        session.execute(stmt)
        session.commit()
        session.close()

#TODO ---> As matrículas de cursos deletados devem ser apgadas também, certo?

    def hard_delete(id):
        session.begin()
        curso = session.get(Cursos, id)
        session.delete(curso)

        session.commit()
        session.close()

    def soft_delete(id):

        stmt = (
            update(Cursos)
            .where(Cursos.id == id)
            .values(deleted=True)
        )

        session.begin()
        session.execute(stmt)
        session.commit()
        session.close()

    def get_alunos(id_curso):

        ids_alunos = session.query(Matriculas.id_aluno).where(Matriculas.id_curso == id_curso)
        alunos = session.query(Alunos).where(Alunos.id in ids_alunos)

        return alunos