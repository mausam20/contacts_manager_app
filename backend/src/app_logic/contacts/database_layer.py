from sqlalchemy.orm import Session
from fastapi import HTTPException
from .user_model import User

def search_users_by_name_or_email(term: str, db: Session):
    return db.query(User).filter(
        (User.name.ilike(f"%{term}%")) | (User.email.ilike(f"%{term}%"))
    ).all()

def save_user(user_data: str, db: Session):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return False
    user = User(email=user_data.email, name=user_data.name, contact=user_data.contact)
    db.add(user)
    db.commit()
    db.refresh(user)
    return True


def delete_user(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
