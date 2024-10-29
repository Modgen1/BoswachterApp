from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends
from typing import Annotated
from os import getenv
from app.models import *

__db_url = getenv("BOSWACHTER_DB_URL")
__engine = create_engine(__db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(__engine)

def __get_session():
    with Session(__engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(__get_session)]