from models.user import User
from sqlalchemy.orm import Session


def create_user(db: Session, name: str) -> User:
    user = User(name=name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()
