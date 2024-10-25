# app/schemas/project.py
from pydantic import BaseModel, HttpUrl
from datetime import datetime

class ProjectBase(BaseModel):
    title: str
    description: str
    image_url: HttpUrl
    project_url: HttpUrl

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class ProjectInDBBase(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class Project(ProjectInDBBase):
    pass
