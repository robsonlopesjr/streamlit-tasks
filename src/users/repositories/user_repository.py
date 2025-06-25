import uuid
from sqlalchemy.orm import Session
from users.models.user_model import User


def get_all(db: Session):
    return db.query(User).all()


def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_by_id(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def create(db: Session, name: str, email: str, hashed_password: str):
    user = User(id=str(uuid.uuid4()), name=name, email=email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user_id: str, name: str, email: str, hashed_password: str):
    user = get_by_id(db, user_id)
    if not user:
        return None
    user.name = name
    user.email = email
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user_id: str):
    user = get_by_id(db, user_id)
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
