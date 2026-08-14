from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker, Session

from pathlib import Path
from dotenv import load_dotenv

import os

load_dotenv()

DATABASE_URL = (
    os.getenv("DATABASE_URL")
)

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set")

#Engine - Connection to the DB
engine = create_engine(
    DATABASE_URL,
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)


#Create the base class for all tables
Base = declarative_base()

def get_db() -> Generator[Session, None, None]:

    db = SessionLocal()

    try: 
        yield db
    
    finally:
        db.close()