from fastapi import FastAPI
from app.api.endpoints import auth, projects  # Include your auth and projects routers
from app.db import Base, engine

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(projects.router)
