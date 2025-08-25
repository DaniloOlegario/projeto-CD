from fastapi import FastAPI, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models, schemas, database
from typing import Optional
import os

# Cria a instância do FastAPI
app = FastAPI()

# Permite que o front-end (no navegador) se comunique com o back-end (sua API)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependência que gerencia a sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota principal da API, agora com um novo parâmetro de filtro
@app.get("/caminhoes/", response_model=list[schemas.Caminhao])
def get_caminhoes(
    loja: Optional[str] = None,
    status_filter: Optional[str] = None, # <-- Novo parâmetro para filtrar por status
    db: Session = Depends(get_db)
):
    """
    Retorna a lista de caminhões do banco de dados, com filtros por loja e status.
    """
    query = db.query(models.Caminhao)
    
    if loja:
        # Se um filtro de loja for fornecido, adiciona-o à consulta
        query = query.filter(models.Caminhao.loja == loja)

    if status_filter == "completo":
        # Se o filtro for 'completo', busca caminhões com 100% ou mais de carregamento
        query = query.filter(models.Caminhao.porcentagem_carregamento >= 100)
    elif status_filter == "incompleto":
        # Se o filtro for 'incompleto', busca caminhões com menos de 100%
        query = query.filter(models.Caminhao.porcentagem_carregamento < 100)
        
    caminhoes = query.all()
    return caminhoes

# Monta os arquivos estáticos (HTML, CSS, JS) para serem exibidos
app.mount("/", StaticFiles(directory=".", html=True), name="static")