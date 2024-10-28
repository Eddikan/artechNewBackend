from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, engine
from alembic import command
from alembic.config import Config
from sqlalchemy.orm import sessionmaker
from app.api.endpoints import auth, projects  # Include your auth and projects routers

app = FastAPI()

# Database session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.on_event("startup")
async def startup_event():
    # Run Alembic migrations
    alembic_cfg = Config("alembic.ini")  # Path to your alembic.ini file
    command.upgrade(alembic_cfg, "head")  # Upgrade to the latest version
    print("Database migrations applied.")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  # Allow all headers; specify if needed
)

# Root endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(projects.router)
