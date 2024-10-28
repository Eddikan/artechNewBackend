from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)  
    description = Column(String)          
    image_url = Column(String)            
    project_url = Column(String)         
    created_at = Column(DateTime, default=datetime.utcnow)  
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)  
