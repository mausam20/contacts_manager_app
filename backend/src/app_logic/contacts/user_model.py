from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    email = Column(String(256), primary_key=True, index=True)
    name = Column(String(100), index=True)
    contact = Column(String(100))