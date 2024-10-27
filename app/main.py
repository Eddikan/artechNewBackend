from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.endpoints import auth, projects  # Include your auth and projects routers
from app.db import Base, engine

app = FastAPI()

# CORS configuration allowing all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(projects.router)

# Custom error handler for 404 Not Found
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "Route not found. Please check your URL."}
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )

# Optional: Catch-all route for unmatched routes
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    return JSONResponse(
        status_code=404,
        content={"message": "Route not found. Please check your URL."}
    )
