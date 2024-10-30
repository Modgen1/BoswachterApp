from sqlmodel import SQLModel, create_engine
from os import getenv
from app.models import *

__db_url = getenv("BOSWACHTER_DB_URL")
engine = create_engine(__db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)