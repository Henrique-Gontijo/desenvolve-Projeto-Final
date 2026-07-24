# Trabalho Final de Backend
Este é o trabalho final de Backend do curso Projeto Desenvolve. Ele consiste em uma API de gerenciamento de alunos, cursos e matrículas.


<br>

## Principais Ferramentas Utilizadas
- **FastAPI**: Consiste em um Framework Web de alta perfomanse para a construção de API's para Python baseado em Type Hints.

  
- **Pydantic**: Biblioteca de validação de dados para Python utilizando-se dos Type Hints do python, na qual o FastAPI se apoia para seu funcionamento.

  
- **SQLAlchemy**: Um kit de trabalho para SQL e ORM, utilizado para a definição e manipulação de tabelas no banco de dados, além de realizar a conexão de maneira simplificada com o banco, funcionando com diversos SGBD's.


<br>

## Tabelas
Realiza do gerenciamento de três tabelas de dados:

### ALUNOS
- id --> INT | PRIMARY KEY | AUTO INCREMENT
- nome --> VARCHAR 200 | UNIQUE KEY | NOT NULL
- email --> VARCHAR 150 | NOT NULL
- deleted --> BOOLEAN | DEFAULT = FALSE

### CURSOS
- id --> INT | PRIMARY KEY | AUTO INCREMENT
- titulo --> VARCHAR 180 | UNIQUE KEY | NOT NULL
- email --> CHAR
- deleted --> BOOLEAN | DEFAULT = FALSE

### MATRICULAS
- id --> INT | PRIMARY KEY | AUTO INCREMENT
- id_curso --> INT | FOREIGN KEY REFERENCES cursos
- id_aluno --> INT | FOREING KEY REFERENCES alunos
- deleted --> BOOLEAN | DEFAULT = FALSE


<br>

## Endpoits
Para cada tabela, há uma série de endpoits disponíveis para a manipulação das tabelas:

- **(GET) /tabela** --> Retorna um JSON contendo a lista de alunos existentes, contidos na chave "data".
- **(GET) /tabela/{id}** --> Exemplo: ```/alunos/5``` retorna os dados do aluno de ID igual a 5, também contidos em um JSON na chave "data".
- **(POST) /tabela/cadastro** --> Envia uma requisição ao banco para a criação de um novo aluno.
- **(PUT) /tabela/{id}/atualizar_dados** --> Exemplo: ```/alunos/5/atualizar_dados```, pode atualizar o nome e o email do aluno de ID 5.
- **(DELETE) /tabela/{id}/deletar** --> Exemplo: ```/alunos/5/deletar``` deleta todos os dados do aluno de ID 5.
- **(DELETE) /tabela/{id}/exluir** --> Exemplo: ```/alunos/5/exluir``` envia os dados do aluno de ID 5 para a lixeira.
- **(GET) /docs** ou **/redoc** --> Concede-lhe acesso à documentação detalhada dos endpoits existentes.

### Além desses, há dois endpoits específicos das tabelas ALUNOS e CURSOS:
- **(GET) /alunos/{id}/cursos** --> Exemplo: ```àlunos/5/cursos``` retorna os cursos em que o aluno de ID 5 está matriculado.
- **(GET) /cursos/{id}/alunos** --> Exemplo: ```cursos/3/alunos``` retorna os alunos matriculados no curso de ID 3.

**OBS**: Para a tabela "matriculas" não há o endpoit ```PUT: /tabela/{id}/atualizar_dados```.


<br>

## Inicializando o Projeto

A seguir, o passo a passo de como inicializar o projeto em sua própria máquina.
**ATENÇÃO**: É necessário possuir o Python 3 pré-instalado em seu computador.

### 1. Preparando Ambiente de Desenvolvimento
- Sobretudo, é necessário criar um ambiente virtual de desenvolvimento, para isso, abra o terminal e acesse a pasta raiz do projeto (a em que está o arquivo requirements.txt) utilizando o comando `cd`, então digite `py -m venv .venv` caso esteja no Windows ou `python3 -m venv .venv` caso esteja em uma distribuição Linux.

  
- Em seguida, deve-se ativar o ambiente, para isso, digite `.venv\Scripts\ativate` caso esteja no Windows (recomendo utilizar o Prompt de Comando ao invés do PowerShell) ou `source .venv/bin/aticvate`.


- Por fim, digite `pip install -r requirements.txt` e espere o processo de instalação das bibliotecas ser completado.



### 2. Realizando conexão com o Banco de Dados

Ainda em processo de construção



### 3. Rodando o projeto localmente

Após completar os passos anteriores, ainda com o ambiente .venv ativo e na pasta raiz, digite `uvicorn app.main:app`, após alguns segundos, aparecerá a seguinte linha no terminal: ***INFO**    Uvicorn running on http://127.0.0.1:8000*, clique ems sobre o link segurando o botão "Ctrl" e será aberta uma página no seu navegador com o projeto em funcionamento. Caso queira realizar requisições HTTP mais complexas (POST, PUT e DELETE), será necessário utilizar alguma outra ferramenta tal como Postman.
