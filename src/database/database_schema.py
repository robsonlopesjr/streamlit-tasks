from pydantic import BaseModel, Field


class MySQLSettings(BaseModel):
    host: str = Field(..., description="Endereço do servidor MySQL")
    port: int = Field(..., description="Porta do banco de dados")
    database: str = Field(..., description="Nome do banco de dados")
    user: str = Field(..., description="Usuário do banco de dados")
    password: str = Field(..., description="Senha do banco de dados")


class SQLServerSettings(BaseModel):
    host: str = Field(..., description="Endereço do servidor SQL Server")
    port: int = Field(..., description="Porta do banco de dados")
    database: str = Field(..., description="Nome do banco de dados")
    user: str = Field(..., description="Usuário do banco de dados")
    password: str = Field(..., description="Senha do banco de dados")
