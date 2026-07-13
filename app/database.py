# IMPORTS
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# load the var from .env
load_dotenv()

# database url from .env
DATABASE_URL = os.getenv("DATABASE_URL")
# create the connection to PostgreSQL
engine = create_engine(url=DATABASE_URL)
# create a temporary conversation with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



