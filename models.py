from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Caminhao(Base):
    __tablename__ = 'caminhoes'

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String, unique=True, index=True)
    capacidade_maxima = Column(Integer)
    paletes_carregados = Column(Integer)
    status = Column(String)
    cor_status = Column(String)
    porcentagem_carregamento = Column(Integer)
    loja = Column(String, nullable=True)