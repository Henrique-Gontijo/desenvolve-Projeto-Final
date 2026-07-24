from sqlalchemy import update
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models.Matriculas import Matriculas
from app.database.models.Alunos import Alunos
from app.database.models.Cursos import Cursos

session: Session = SessionLocal()
session.begin()

class MatriculasHandler():
    '''
    Classe de manipulação da tabela "matriculas" a nível do banco de dados.

    Métodos:
        - create
        - get_all
        - get_byId
        - soft_delete
        - hard_delete
    ''' 

    def create( id_curso: int, id_aluno: int) -> dict:
        '''
        Cria uma nova matrícula no banco de dados.

        Parâmetros:
            - id_curso (int) --> ID do curso em que o aluno será matriculado
            - id_aluno (int)  --> ID do aluno a ser matriculado no curso

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

        aluno = session.query(Alunos).where(Alunos.deleted == False).where(Alunos.id == id_aluno).first()
        curso = session.query(Cursos).where(Cursos.deleted == False).where(Cursos.id == id_curso).first()

        if (not aluno or aluno == {}) or (not curso or curso == {}):

            if (not aluno or aluno == {}) and (not curso or curso == {}):
                message = "Curso e aluno inexistentes."
            
            elif not aluno or aluno == {}:
                message = "Aluno inexistente."
            
            else:
                message = "Curso inexistente."

            return {
                "status": "Error",
                "status_code": 404,
                "message": message
            }

        matricula = (
            session.query(Matriculas)
            .where(Matriculas.id_curso==id_curso)
            .where(Matriculas.id_aluno==id_aluno).first()
        )

        if matricula and matricula != {}:
            return {
                "status": "Error",
                "status_code": 409,
                "message": "Matrícula já existente."
            }

        new_matricula = Matriculas(id_curso, id_aluno)
        session.add(new_matricula)
        session.commit()

        return {
            "status": "Successful",
            "message": "Matrícula criada com sucesso."
        }

    def get_all() -> dict:
        '''
        Retorna uma lista das matrículas existentes.

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (list[dict]) --> Lista de dicionários com as matrículas
        '''

        response = session.query(Matriculas).where(Matriculas.deleted == False).all()

        if not response:
            return {
                "status": "Error",
                "status_code": 500,
                "message": "Erro desconhecido ao tentar listar as matriculas.",
                "data": None
            }

        return {
            "status": "Successful",
            "message": "Matriculas listasdas com sucesso.",
            "data": response
        }


    def get_byId(id: int) -> dict:
        '''
        Retorna uma matrícula específica no banco de dados.

        Parâmetros:
            - id (int) --> ID da matrícula no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (dict) --> Dicionário com a matrícula
        '''

        response = session.get(Matriculas, id)

        if not response or response == {} or response.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Matrícula não encontrada.",
                "data": None
            }

        return {
            "status": "Successful",
            "message": "Matrícula encontrada com sucesso.",
            "data": response
        }

    def hard_delete(id: int) -> dict:
        '''
        Apaga a matrícula cujo ID foi fornecido.

        Parâmetros:
            - id (int) --> ID da matrícula que será apagada

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

        #TODO --> Hard Delete On Cascade (Será que dá para fazer com relationship?)
        
        matricula = session.get(Matriculas, id)

        if not matricula or matricula == {}:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Matrícula não encontrada."
            }

        session.delete(matricula)
        session.commit()

        return {
            "status": "Successful",
            "message": "Matrícula deletada com sucesso."
        }

    def soft_delete(id: int) -> dict:
        '''
        Marca a coluna "deleted" da matrícula como True, informando que ela foi para a lixeira, 
        mas ainda pode ser recuperada.

        Parâmetros:
            - id (int) --> ID da matrícula no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

        #TODO --> Soft Delete On Cascade

        matricula = session.get(Matriculas, id)

        if not matricula or matricula == {} or matricula.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Matrícula não encontrada."
            }
        
        stmt = (
            update(Matriculas)
            .where(Matriculas.id == id)
            .values(deleted=True)
        )

        session.execute(stmt)
        session.commit()

        return {
            "status": "Successful",
            "message": "Soft Delete executado com sucesso."
        }

session.close()