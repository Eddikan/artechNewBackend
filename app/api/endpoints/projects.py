from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.project import Project
from pydantic import BaseModel
from typing import List
from fastapi.security import OAuth2PasswordBearer, HTTPBearer, HTTPBasicCredentials


router = APIRouter()
oauth2_scheme = HTTPBearer()


class ProjectCreate(BaseModel):
    title: str
    description: str
    image_url: str
    project_url: str


class ProjectOut(ProjectCreate):
    id: int


@router.get("/projects", response_model=List[ProjectOut])
def get_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    projects = db.query(Project).offset(skip).limit(limit).all()
    return projects


@router.get("/projects/{id}", response_model=ProjectOut)
def get_project(id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/projects", response_model=ProjectOut)
def create_project(project: ProjectCreate, db: Session = Depends(get_db), token: HTTPBasicCredentials = Depends(oauth2_scheme)):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.put("/projects/{id}", response_model=ProjectOut)
def update_project(id: int, project: ProjectCreate, db: Session = Depends(get_db), token: HTTPBasicCredentials = Depends(oauth2_scheme)):
    db_project = db.query(Project).filter(Project.id == id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in project.dict().items():
        setattr(db_project, key, value)

    db.commit()
    db.refresh(db_project)
    return db_project


@router.delete("/projects/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(id: int, db: Session = Depends(get_db), token: HTTPBasicCredentials = Depends(oauth2_scheme)):
    db_project = db.query(Project).filter(Project.id == id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(db_project)
    db.commit()
