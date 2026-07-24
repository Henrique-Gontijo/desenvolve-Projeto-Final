from typing import Optional

from sqlalchemy import update
from sqlalchemy.orm import Session

from app.database.connection import SessionLocal
from app.database.models.Cursos import Cursos
from app.database.models.Alunos import Alunos
from app.database.models.Matriculas import Matriculas

session: Session = SessionLocal()
session.begin()

class CursosHandler():
    '''
    Classe de manipulação da tabela "cursos" a nível do banco de dados.

    Métodos:
        - create
        - get_all
        - get_byId
        - get_alunos
        - update
        - soft_delete
        - hard_delete
    '''


    def create( titulo: str, descricao: Optional[str] = None):
        '''
        Cria um novo curso no banco de dados.

        Parâmetros:
            - titulo (str) --> Título do curso
            - descricao (Optional[str]) --> Descrição do curso

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

    
        curso = session.query(Cursos).where(Cursos.titulo==titulo).first()

        if curso and curso != {}:
            return {
                "status": "Error",
                "status_code": 409,
                "message": "Curso já existente."
            }
        
        new_curso = Cursos(titulo, descricao)
        session.add(new_curso)

        session.commit()

        return {
            "status": "Successful",
            "message": "Curso criado com sucesso."
        }

    def get_all() -> dict:
        '''
        Retorna uma lista com os dados dos cursos.

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (list[dict]) --> Lista de dicionários com os dados dos cursos
        '''
    
        response = session.query(Cursos).where(Cursos.deleted == False).all()

        if not response:
            return {
                "status": "Error",
                "status_code": 500,
                "message": "Erro desconhecido ao tentar listar os cursos.",
                "data": None
            }

        return {
            "status": "Successful",
            "message": "Cursos listados com sucesso.",
            "data": response
        }

    def get_byId(id: int) -> dict:
        '''
        Retorna um curso específico no banco de dados.

        Parâmetros:
            - id (int) --> ID do curso no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (dict) --> Dicionário com os dados do curso
        '''
    
        response = session.get(Cursos, id)

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

    def update(id: int, titulo: Optional[str] = None, descricao: Optional[str] = None) -> dict:
        '''
        Atualiza os dados de curso no banco. Com exceção do ID, os dados de atualização são opcionais.
        Quando algum deles não é fornecido, a função simplesmente não atualiza o dado omisso.

        Parâmetros:
            - id (int) -> ID do curso cujos dados serão atualizados
            - titulo (str) [Optional] --> Novo título do curso
            - descricao (str) [Optional] --> Nova descrição do curso

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

        curso = session.get(Cursos, id)

        if not curso or curso == {} or curso.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Curso não encontrado.",
            }

        curso_diferente = session.query(Cursos).where(Cursos.titulo==titulo).first()

        if curso_diferente and curso_diferente.id != id:
            return {
                "status": "Error",
                "status_code": 409,
                "message": "Já existe um curso com este título."
            }

        new_titulo = titulo if titulo and titulo != "" else curso.titulo
        new_descricao = descricao if descricao and descricao != "" else curso.descricao

        stmt = (
            update(Cursos)
            .where(Cursos.id == id)
            .values(titulo=new_titulo, descricao=new_descricao)
        )

        session.execute(stmt)
        session.commit()

        return {
            "status": "Successful",
            "message": "Dados atualizados com sucesso."
        }

    def hard_delete(id: int) -> dict:
        '''
        Apaga os dados do curso cujo ID foi fornecido.

        Parâmetros:
            - id (int) --> ID do curso cujos dados serão apagados

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''
    
        #TODO --> Hard Delete On Cascade (Será que dá para fazer com relationship?)

        curso = session.get(Cursos, id)

        if not curso or curso == {}:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Curso não encontrado."
            }

        session.delete(curso)
        session.commit()

        return {
            "status": "Successful",
            "message": "Curso deletado com sucesso."
        }

    def soft_delete(id: int) -> dict:
        '''
        Marca a coluna "deleted" do curso como True, informando que seus dados foram para a lixeira, 
        mas ainda podem ser recuperados.

        Parâmetros:
            - id (int) --> ID do curso no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
        '''

        #TODO --> Soft Delete On Cascade

        curso = session.get(Cursos, id)

        if not curso or curso == {} or curso.deleted == True:
            return {
                "status": "Error",
                "status_code": 404,
                "message": "Curso não encontrado."
            }

        stmt = (
            update(Cursos)
            .where(Cursos.id == id)
            .values(deleted=True)
        )

        session.execute(stmt)
        session.commit()

        return {
            "status": "Successful",
            "message": "Soft Delete executado com sucesso."
        }

     #TODO --> Consertar essa bagaça de get_alunos ------------------------------------------------------------
    #TODO --> Adicionar retorno correto ----------------------------------------------------------------------

    def get_alunos(id: int) -> dict:
        '''
        Retorna a lista de alunos matriculados no curso.

        Parâmetros:
            - id (int) --> ID do aluno no banco

        Retorno (dict):
            - status (str) --> Indica se operação ocorreu normamente (Successful) ou se houve algum erro (Error)
            - status_code (int) --> Em caso de erro, o código HTTP relacionado a ele
            - message (str) --> Mensagem relacionada a operação
            - data (list[dict]) --> Lista de dicionários dos alunos
        '''        

        ids_alunos = (
            session.query(Matriculas.id_aluno).where(Matriculas.deleted == False)
            .where(Matriculas.id_curso == id).all()
        )

        #alunos = session.query(Alunos).where(Alunos.id.in_(ids_alunos)).all()

        return ids_alunos
    
session.close()