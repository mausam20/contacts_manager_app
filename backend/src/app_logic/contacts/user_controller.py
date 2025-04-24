from sqlalchemy.orm import Session
from .user_model import User
from fastapi import HTTPException
from .response_schema import UserCreate
from . import database_layer

def search_users(search_term: str, db: Session):
    return database_layer.search_users_by_name_or_email(search_term, db)

def save_user(user_data: UserCreate, db: Session):
    is_save = database_layer.save_user(user_data, db)
    if is_save:
        return {"message": "User saved successfully"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")

def delete_user(email: str, db: Session):
    is_delete = database_layer.delete_user(email, db)
    if is_delete:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=400, detail="User not found")