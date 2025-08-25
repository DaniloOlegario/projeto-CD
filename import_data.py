import pandas as pd
from sqlalchemy import create_engine
import models
from database import SessionLocal

# 1. Defina o nome do seu arquivo XLSX
file_path = 'dados.xlsx' 

# 2. Leia o arquivo XLSX
try:
    df = pd.read_excel(file_path)
    print("Planilha lida com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    exit()

# 3. Conecte-se ao banco de dados
engine = create_engine(models.DATABASE_URL)
models.Base.metadata.create_all(bind=engine)
db = SessionLocal()

# 4. Processar cada linha da planilha e salvar no banco de dados
for index, row in df.iterrows():
    # Crie um novo objeto Caminhao ou use o existente
    caminhao = db.query(models.Caminhao).filter(models.Caminhao.placa == row['placa']).first()
    if not caminhao:
        caminhao = models.Caminhao(placa=row['placa'])
        db.add(caminhao)

    # Atualize os dados do caminhão com as informações da planilha
    caminhao.loja = row['loja']
    caminhao.status = row['status']
    caminhao.paletes_carregados = row['paletes_carregados']
    caminhao.capacidade_maxima = row['capacidade_maxima']
    caminhao.porcentagem_carregamento = row['porcentagem_carregamento']
    caminhao.cor_status = row['cor_status']

# 5. Salve as mudanças no banco de dados
db.commit()
db.close()

print("Dados da planilha importados para o banco de dados com sucesso!")