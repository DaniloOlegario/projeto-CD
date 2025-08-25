from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define o nome do arquivo do banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///automacao.db"

# Cria o motor de banco de dados
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cria a classe SessionLocal para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a classe Base para modelos de banco de dados
Base = declarative_base()