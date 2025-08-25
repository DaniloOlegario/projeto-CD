import pandas as pd
from sqlalchemy.orm import Session
from datetime import datetime

import database
import models

def calcular_status_caminhao(paletes_carregados, capacidade_maxima):
    """Calcula o status e a porcentagem de carregamento do caminhão."""
    if capacidade_maxima <= 0:
        return 0, "Disponível", "gray"

    porcentagem = (paletes_carregados / capacidade_maxima) * 100
    
    if porcentagem >= 100:
        status = "Carregado"
        cor = "green"
    elif porcentagem > 0:
        status = "Em Andamento"
        cor = "yellow"
    else:
        status = "Disponível"
        cor = "gray"
    
    return int(porcentagem), status, cor

def sincronizar_dados():
    """Lê a planilha e sincroniza os dados com o banco de dados."""
    try:
        # Lê a planilha Excel
        df = pd.read_excel('planilha_automacao.xlsx')
    except FileNotFoundError:
        print("Erro: O arquivo 'planilha_automacao.xlsx' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")
        return

    db: Session = database.SessionLocal()

    try:
        # Dicionário para armazenar as placas da planilha
        placas_da_planilha = set(df['placa'].dropna().unique())
        
        # Percorre as linhas da planilha
        for index, row in df.iterrows():
            placa = str(row['placa']).strip()
            capacidade_maxima = int(row['capacidade_maxima'])
            paletes_carregados = int(row['paletes_carregados'])
            loja = str(row['loja']).strip() if pd.notna(row['loja']) else None

            # Calcula o status e a porcentagem
            porcentagem, status, cor = calcular_status_caminhao(paletes_carregados, capacidade_maxima)

            # Busca o caminhão no banco de dados
            caminhao_existente = db.query(models.Caminhao).filter(models.Caminhao.placa == placa).first()

            if caminhao_existente:
                # Atualiza se houver necessidade
                caminhao_existente.capacidade_maxima = capacidade_maxima
                caminhao_existente.paletes_carregados = paletes_carregados
                caminhao_existente.porcentagem_carregamento = porcentagem
                caminhao_existente.status = status
                caminhao_existente.cor_status = cor
                caminhao_existente.loja = loja
            else:
                # Cria um novo caminhão
                novo_caminhao = models.Caminhao(
                    placa=placa,
                    capacidade_maxima=capacidade_maxima,
                    paletes_carregados=paletes_carregados,
                    porcentagem_carregamento=porcentagem,
                    status=status,
                    cor_status=cor,
                    loja=loja
                )
                db.add(novo_caminhao)

        # Deleta caminhões que não estão mais na planilha
        placas_no_banco = [c.placa for c in db.query(models.Caminhao).all()]
        for placa in placas_no_banco:
            if placa not in placas_da_planilha:
                caminhao_a_deletar = db.query(models.Caminhao).filter(models.Caminhao.placa == placa).first()
                db.delete(caminhao_a_deletar)

        db.commit()
        print(f"Sincronização concluída com sucesso. Total de caminhões na planilha: {len(placas_da_planilha)}")
    except Exception as e:
        db.rollback()
        print(f"Ocorreu um erro durante a sincronização: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    sincronizar_dados()