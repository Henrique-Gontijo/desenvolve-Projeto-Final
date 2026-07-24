from sqlalchemy import create_engine
from sqlalchemy.orm import ( declarative_base, sessionmaker )

Base = declarative_base()

engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

# Fábrica de Session (Configuração)
SessionLocal = sessionmaker(autocommit = False, bind=engine)