from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema para a resposta da API - Visualização
class Caminhao(BaseModel):
    id: int
    placa: str
    capacidade_maxima: int
    paletes_carregados: int
    status: str
    cor_status: str
    porcentagem_carregamento: int
    loja: Optional[str]

    class Config:
        from_attributes = True