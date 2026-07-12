# auth/service.py
# Business logic layer - now backed by SQLite via SQLAlchemy

from sqlalchemy.orm import Session

from auth.security import hash_password, verify_password
from auth.schemas import UserRegister
from auth.models import User


def get_user_by_username(db: Session, username: str) -> User | None:
    return db.query(User).filter(User.username == username).first()


def register_user(db: Session, user_data: UserRegister) -> User:
    if get_user_by_username(db, user_data.username):
        raise ValueError("Username already registered.")

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
