from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import user, password, host
from zit_app import read_products

SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}/test'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_get_products():
    read_products()