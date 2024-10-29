from sqlmodel import Session, SQLModel, create_engine
from fastapi import Depends
from typing import Annotated
from app.models import *

# @todo replace with postgresDB
__sqlite_file_name = "../database.db"
__sqlite_url = f"sqlite:///{__sqlite_file_name}"
__connect_args = {"check_same_thread": False}
__engine = create_engine(__sqlite_url, connect_args=__connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(__engine)

def __get_session():
    with Session(__engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(__get_session)]