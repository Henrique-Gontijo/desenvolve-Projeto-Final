from typing import Optional

from sqlalchemy import update
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
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

    def create( nome: str, email: str) -> dict:
        '''
        Cria um novo aluno no banco de dados.

        Parâmetros:
            - nome (str) --> Nome do Aluno
            - email (str)  --> Email do aluno

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
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

    def get_all() -> dict:
        '''
        Retorna uma lista com os dados dos alunos cadastrados no curso.

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (list[dict]) --> Lista de dicionários com os dados dos alunos
        '''

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

    def get_byId(id: int) -> dict:
        '''
        Retorna um aluno específico no banco de dados.

        Parâmetros:
            - id (int) --> ID do aluno no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (dict) --> Dicionário com os dados do aluno
        '''

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

    def update(id: int, nome: Optional[str] = None, email: Optional[str] = None) -> dict:
        '''
        Atualiza os dados de aluno no banco. Com exceção do ID, os dados de atualização são opcionais.
        Quando algum deles não é fornecido, a função simplesmente não atualiza o dado omisso.

        Parâmetros:
            - id (int) -> ID do aluno cujos dados serão atualizados
            - nome (str) [Optional] --> Novo nome do aluno
            - email (str) [Optional] --> Novo email do aluno

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''
        aluno = session.get(Alunos, id)

        if not aluno or aluno == {} or aluno.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Aluno não encontrado.",
            }

        aluno_diferente = session.query(Alunos).where(Alunos.nome==nome).first()

        if aluno_diferente and aluno_diferente.id != id:
            return {
                "status": "Error",
                "status_code": 409,
                "message": "Já existe outro aluno com esse nome."
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

    def hard_delete(id: int) -> dict:
        '''
        Apaga os dados do aluno cujo ID foi fornecido.

        Parâmetros:
            - id (int) --> ID do aluno cujos dados serão apagados

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

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
            "message": "Aluno deletado com sucesso."
        }

    def soft_delete(id) -> dict:
        '''
        Marca a coluna "deleted" do aluno como True, informando que seus dados foram para a lixeira, 
        mas ainda podem ser recuperados.

        Parâmetros:
            - id (int) --> ID do aluno no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

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

    def get_cursos(id: int) -> dict:
        '''
        Retorna a lista de cursos em que o aluno está matriculado.

        Parâmetros:
            - id (int) --> ID do aluno no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (list[dict]) --> Lista de dicionários dos cursos
        '''

        ids_cursos = (
            session.query(Matriculas.id_curso).where(Matriculas.deleted == False)
            .where(Matriculas.id_aluno == id).all()
        )
        #cursos = session.query(Cursos).where(Cursos.id.in_(ids_cursos)).all()

        return ids_cursos
    
session.close()