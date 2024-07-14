from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    title = Column(String, index=True, nullable=True)
    text = Column(String, index=True, nullable=True)
