
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, engine
from app.api.endpoints import auth, projects  # Include your auth and projects routers


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],  # Allow all headers; specify if needed
)
# Root endpoint for testing
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# Create the database tables
Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(projects.router)