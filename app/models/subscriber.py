from sqlalchemy import Column, Integer, String
from app.db import Base

class Subscriber(Base):
    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True, autoincrement=True)  # This should not throw a warning
    email = Column(String, unique=True, nullable=False)
