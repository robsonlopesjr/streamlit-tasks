from users.schemas.user_schema import UserCreate
from users.services import user_service


def criar_usuario(nome, email, senha):
    user = UserCreate(name=nome, email=email, password=senha)
    return user_service.criar_usuario(user)


def atualizar_usuario(user_id, nome, email, senha):
    user = UserCreate(name=nome, email=email, password=senha)
    return user_service.atualizar_usuario(user_id, user)


def excluir_usuario(user_id):
    return user_service.excluir_usuario(user_id)


def listar_usuarios():
    return user_service.listar_usuarios()
