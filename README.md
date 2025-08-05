# API Backend - FastAPI

Este é um projeto de API backend desenvolvido com **FastAPI**, utilizando **Swagger** para documentação automática e **Alembic** para controle de migrações do banco de dados.

## 🚀 Tecnologias utilizadas

- **FastAPI** – Framework moderno e rápido para construção de APIs em Python
- **Swagger UI** – Documentação interativa embutida via OpenAPI
- **Alembic** – Migrations para banco de dados
- **SQLAlchemy** – ORM para manipulação do banco
- **Uvicorn** – Servidor ASGI leve e rápido

---

## 📦 Como rodar o projeto localmente

### Pré-requisitos

- Python 3.10+
- PostgreSQL (ou outro banco configurado no seu `.env`)
- Virtualenv (recomendado)

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto

# 2. Crie e ative o ambiente virtual
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o arquivo .env com as variáveis do banco

# 5. Rode as migrações
alembic upgrade head

# 6. Inicie o servidor
uvicorn app.main:app --reload
