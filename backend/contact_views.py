from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from src.app_logic.contacts import user_controller as user_controller
from src.app_logic.contacts.response_schema import UserCreate, UserResponse, DeleteResponse
from typing import List

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get("/search/{search_term}", response_model=List[UserResponse])
def search_users(search_term: str, db: Session = Depends(get_db)):
    return user_controller.search_users(search_term, db)

@router.post("/save", response_model=UserResponse)
def save_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return user_controller.save_user(user_data, db)

@router.get("/delete/{email}", response_model=DeleteResponse)
def delete_user(email: str, db: Session = Depends(get_db)):
    return user_controller.delete_user(email, db)
