import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import ( declarative_base, sessionmaker )

#Carregando variáveis de ambiente no arquivo .env
load_dotenv()

# Buscando string de conexão no arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

Base = declarative_base()

engine = create_engine(DATABASE_URL)

# Fábrica de Session (Configuração)
SessionLocal = sessionmaker(autocommit = False, bind=engine)