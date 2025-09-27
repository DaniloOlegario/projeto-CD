# 🚚 API de Monitoramento de Status de Caminhões (FastAPI/SQLAlchemy)

## 🎯 Visão Geral

Este projeto é uma **API RESTful** desenvolvida em **FastAPI** para gerenciar e monitorar o status de viagens de caminhões em um Centro de Distribuição (CD). Ele simula um *pipeline* de dados onde informações operacionais são coletadas, armazenadas em **SQL** e transformadas em métricas de BI.

**Destaques:**
* **Modelagem de Dados:** Uso de SQLAlchemy para criar tabelas e relações (`Caminhoes` e `Viagens`).
* **Transformação de Dados:** Cálculo da `% de Carregamento` em tempo real na criação de cada registro.
* **Endpoints de Análise:** Rota específica para extração de dados filtrados (`/viagens/`) e resumos estatísticos.

---

## 🛠️ Tecnologias Utilizadas

* **FastAPI:** Framework de alto desempenho para criação da API.
* **SQLAlchemy:** ORM (Mapeador Objeto-Relacional) para manipulação eficiente do banco de dados (SQLite).
* **Python/Pandas:** Utilizado no script de importação (`import_data.py`) para ETL (Extração, Transformação e Carga) de dados a partir de uma planilha (.xlsx).
* **Uvicorn:** Servidor ASGI.

---

## 🚀 Funcionalidades da API

A API permite gerenciar e consultar os dados através dos seguintes *endpoints*:

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| **POST** | `/viagens/` | Cria um novo registro de viagem, **calculando a % de carregamento** e vinculando à placa do caminhão (relação de banco de dados). |
| **GET** | `/viagens/` | Retorna a lista de todas as viagens. Suporta filtros por `loja` e `status`. |
| **GET** | `/viagens/summary` | **(Análise de Dados/BI)** Retorna o total de viagens, a média de carregamento e a contagem de viagens por status. |
| **POST** | `/import-data/` | Limpa e importa novos dados de uma planilha (`planilha_automacao.xlsx`). |

## ⚙️ Como Executar

1.  Clone o repositório.
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Inicie a API: `uvicorn app:app --reload`
4.  Acesse a documentação interativa para testes: `http://127.0.0.1:8000/docs`

---
