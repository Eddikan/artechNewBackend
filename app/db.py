# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Create the engine for connecting to SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is the session we’ll use to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is the class that our models will inherit from
Base = declarative_base()

# Dependency to get the session for database operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
