from database.connection import SessionLocal
from users.repositories import user_repository
from users.schemas.user_schema import UserCreate
from users.utils.password_utils import generate_password_hash


def criar_usuario(dados: UserCreate):
    db = SessionLocal()
    try:
        if user_repository.get_by_email(db, dados.email):
            raise ValueError("Email já cadastrado.")
        senha_hash = generate_password_hash(dados.password)
        return user_repository.create(db, dados.name, dados.email, senha_hash)
    finally:
        db.close()


def listar_usuarios():
    db = SessionLocal()
    try:
        return user_repository.get_all(db)
    finally:
        db.close()


def atualizar_usuario(user_id: str, dados: UserCreate):
    db = SessionLocal()
    try:
        senha_hash = generate_password_hash(dados.password)
        user = user_repository.update(db, user_id, dados.name, dados.email, senha_hash)
        if not user:
            raise ValueError("Usuário não encontrado.")
        return user
    finally:
        db.close()


def excluir_usuario(user_id: str):
    db = SessionLocal()
    try:
        user = user_repository.delete(db, user_id)
        if not user:
            raise ValueError("Usuário não encontrado.")
        return user
    finally:
        db.close()
