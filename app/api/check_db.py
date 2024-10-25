from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import get_db  # Assuming get_db is set up to provide a DB session
from app.models.user import User  # Adjust model import based on your structure
from app.models.project import Project

router = APIRouter()

@router.get("/check-db/users")
def check_db_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": users}

@router.get("/check-db/projects")
def check_db_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()
    return {"projects": projects}