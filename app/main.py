
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, engine
from app.api.endpoints import auth, projects  # Include your auth and projects routers


app = FastAPI()

# CORS settings
origins = [
    "https://artech-test-frontend.vercel.app/",  # Replace with your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],  # Allow all headers; specify if needed
)

# Create the database tables
Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(projects.router)