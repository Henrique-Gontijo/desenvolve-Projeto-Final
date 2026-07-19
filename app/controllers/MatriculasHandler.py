from sqlalchemy import update
from sqlalchemy.orm import Session

from app.database.connection import (SessionLocal)
from app.database.models.Matriculas import Matriculas

session: Session = SessionLocal()


class MatriculasHandler():    

#TODO ---> A matrícula em questão já existe?
#TODO ---> Afinal, o aluno e o curso existem no fim das contas?

    def create( id_curso: int, id_aluno: int):
        matricula = Matriculas(id_curso, id_aluno)

        session.begin()
        session.add(matricula)

        session.commit()
        session.close()

#TODO --> As matrículas marcadas como "deleted" devem ser listados?

    def get_all():
        session.begin()
        response = session.query(Matriculas).all()
        session.close()

        return response
    
#TODO ---> O que acontece se nenhuma matricula for encontrada? (get_byId, update, hard_delete e soft_delete)


    def get_byId(id: int):
        session.begin()
        response = session.get(Matriculas, id)
        session.close()

        return response

    def hard_delete(id):
        session.begin()
        matricula = session.get(Matriculas, id)
        session.delete(matricula)

        session.commit()
        session.close()

    def soft_delete(id):

        stmt = (
            update(Matriculas)
            .where(Matriculas.id == id)
            .values(deleted=True)
        )

        session.begin()
        session.execute(stmt)
        session.commit()
        session.close()