from database.connection import Base, engine, SessionLocal
from users.models.user_model import User
from users.utils.password_utils import generate_password_hash
from tasks.models.task_model import Task


def inicializar_banco():
    # Cria as tabelas com base nos models declarados com SQLAlchemy
    Base.metadata.create_all(bind=engine)

    # Cria uma sessão do banco
    db = SessionLocal()

    # Cria o primeiro usuário se ainda não houver nenhum no banco
    if db.query(User).first() is None:
        senha_hash = generate_password_hash("123456")
        user = User(
            name="admin",
            email="admin@teste.com",
            password=senha_hash
        )
        db.add(user)
        db.commit()

    # Finaliza a sessão
    db.close()
