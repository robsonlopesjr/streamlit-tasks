from sqlalchemy.orm import Session
from users.models.user_model import User
from users.utils.password_utils import check_password


class AuthenticationService:
    def __init__(self, db: Session):
        self.db = db

    def autenticar_usuario(self, email: str, senha: str):
        usuario = self.db.query(User).filter(User.email == email).first()

        if not usuario:
            return None  # Usuário não encontrado

        if not check_password(senha, usuario.password):
            return None  # Senha incorreta

        return {
            "id": usuario.id,
            "nome": usuario.name,
            "email": usuario.email
        }
