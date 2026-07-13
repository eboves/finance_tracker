# IMPORTS
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from app.database import Base
from sqlalchemy.sql import func

# Base is how SQLalchemy knows is a table
class User(Base):

    # table name
    __tablename__ = "users"

    # createing the columns of the table
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)
    email = Column(String(100), nullable=False, index=True, unique=True)
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, index=True, default=True)
    # server_default=func.now() --> tell PostgreSQL to fill this itself when creating it
    created = Column(DateTime(timezone=True), server_default=func.now())



