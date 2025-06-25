import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_TYPE, SECRETS_KEY
from database.database_schema import MySQLSettings, SQLServerSettings


def get_engine() -> Engine:
    if DB_TYPE == "sqlite":
        # URL de conexão com o banco de dados SQLite (arquivo local chamado despesas.db)
        DATABASE_URL = "sqlite:///despesas.db"

        # 🔗 Cria o mecanismo de conexão com o banco
        # O argumento `check_same_thread=False` permite usar a mesma conexão em múltiplas threads (necessário no Streamlit)
        return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

    elif DB_TYPE == "mysql":
        creds = MySQLSettings(**st.secrets[SECRETS_KEY["mysql"]])

        DATABASE_URL = f"mysql+pymysql://{creds.user}:{creds.password}@{creds.host}:{creds.port}/{creds.database}"
        return create_engine(DATABASE_URL)

    elif DB_TYPE == "sqlserver":
        creds = SQLServerSettings(**st.secrets[SECRETS_KEY["sqlserver"]])

        DATABASE_URL = f"mssql+pyodbc://{creds.user}:{creds.password}@{creds.host}/{creds.database}?driver=ODBC+Driver+17+for+SQL+Server"
        return create_engine(DATABASE_URL)

    else:
        raise ValueError(f"Tipo de banco de dados não suportado: {DB_TYPE}")


# 🧪 Cria a engine com base nas configurações
engine = get_engine()

# 🧾 Cria uma fábrica de sessões — é com `SessionLocal()` que você acessa o banco nas funções
SessionLocal = sessionmaker(bind=engine)

# 🧱 Base usada para declarar os modelos (tabelas) do SQLAlchemy
# Todos os modelos devem herdar dela: class User(Base): ...
Base = declarative_base()
