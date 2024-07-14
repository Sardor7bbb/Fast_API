from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://postgres:4868@localhost:5432/fast_api")

Base = declarative_base()
session = sessionmaker()


