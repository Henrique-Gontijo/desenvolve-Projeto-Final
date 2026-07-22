from sqlalchemy import update, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

from app.database.connection import (SessionLocal)
from app.database.models.Alunos import Alunos
from app.database.models.Cursos import Cursos
from app.database.models.Matriculas import Matriculas

session: Session = SessionLocal()
session.begin()

#TODO --> Terminar documentação por docstrings!!!!! --------------------------------------------------------

class AlunosHandler():
    '''
    Classe de manipulação da tabela "alunos" a nível do banco de dados.

    Métodos:
        - create
        - get_all
        - get_byId
        - get_cursos
        - update
        - soft_delete
        - hard_delete
    '''

    def create( nome: str, email: str):
        '''
        Cria um novo aluno no banco de dados.

        Parâmetros:
            - nome (str) --> Nome do Aluno
            - email (str)  --> Email do aluno

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - message (str) --> Mensagem relacionada a operação
        '''

        aluno = session.query(Alunos).where(Alunos.nome==nome).first()

        if aluno and aluno != {}:
            return {
                "status": "Error",
                "status_code": 409,
                "message": "Aluno já existente."
            }

        new_aluno = Alunos(nome, email.lower())
        session.add(new_aluno)
        session.commit()

        return {
            "status": "Successful",
            "message": "Aluno criado com sucesso."
        }

    def get_all():
        response = session.query(Alunos).where(Alunos.deleted == False).all()

        if not response:
            return {
                "status": "Error",
                "status_code": 500,
                "message": "Erro desconhecido ao tentar listar os cursos.",
                "data": None
            }

        return {
            "status": "Successful",
            "message": "Alunos listados com sucesso.",
            "data": response
        }

    def get_byId(id: int):

        response = session.get(Alunos, id)

        if not response or response == {} or response.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Aluno não encontrado.",
                "data": None
            }

        return {
            "status": "Successful",
            "message": "Aluno encontrado com sucesso.",
            "data": response
        }

    def update(id: int, nome: str = None, email: str = None):
        aluno = session.get(Alunos, id)

        if not aluno or aluno == {} or aluno.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Aluno não encontrado.",
            }

        new_nome = nome if nome and nome != "" else aluno.nome
        new_email = email if email and email != "" else aluno.email

        stmt = (
            update(Alunos)
            .where(Alunos.id == id)
            .values(nome=new_nome, email=new_email)
        )

        session.execute(stmt)
        session.commit()

        return {
            "status": "Successful",
            "message": "Dados atualizados com sucesso."
        }

    def hard_delete(id):
        aluno = session.get(Alunos, id)

        #TODO --> Hard Delete On Cascade (Será que dá para fazer com relationship?)

        #TODO --> Verificar o porquê desta query esstar retornando uma lista de objetos vazios
        matriculas = session.query(Matriculas.id).where(Matriculas.deleted == False).where(Matriculas.id_aluno == id).all()

        if not aluno or aluno == {}:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Aluno não encontrado." 
            }

        session.delete(aluno)
        session.commit()

        return {
            "status": "Successful",
            "message": "Aluno deletado com sucesso.",
            "matriculas": matriculas[1]
        }

    def soft_delete(id):

        #TODO --> Soft Delete On Cascade

        #TODO --> Verificar o porquê desta query esstar retornando uma lista de objetos vazios
        matriculas = session.query(Matriculas).where(Matriculas.deleted == False).where(Matriculas.id_aluno == id).all()

        aluno = session.get(Alunos, id)

        if not aluno or aluno == {} or aluno.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Aluno não encontrado."
            }

        stmt = (
            update(Alunos)
            .where(Alunos.id == id)
            .values(deleted=True)
        )

        session.execute(stmt)
        session.commit()

        return {
            "status": "Successful",
            "message": "Soft Delete executado com sucesso.",
            "matriculas": matriculas[1]
        }

    #TODO --> Consertar essa bagaça de get_cursos ------------------------------------------------------------
    #TODO --> Adicionar retorno correto ----------------------------------------------------------------------

    def get_cursos(id):

        ids_cursos = (
            session.query(Matriculas.id_curso).where(Matriculas.deleted == False)
            .where(Matriculas.id_aluno == id).all()
        )
        #cursos = session.query(Cursos).where(Cursos.id.in_(ids_cursos)).all()

        return ids_cursos
    
session.close()