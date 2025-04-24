from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    contact: str

class UserCreate(UserBase):
    email: EmailStr

class UserResponse(UserBase):
    email: EmailStr

    class Config:
        orm_mode = True

class DeleteResponse(BaseModel):
    message: str