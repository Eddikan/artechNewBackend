from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user import User, UserCreate, UserResponse
from app.models.user import User
from app.core.config import settings
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

# Function to hash passwords


def hash_password(password: str):
    return pwd_context.hash(password)

# Function to create JWT tokens


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


# Specify response model
@router.post("/auth/signup", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username already exists
    params = jsonable_encoder(user, exclude_none=True)

    db_user = db.query(User).filter(
        User.username == params['username']).first()
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered")

    # Hash the password
    hashed_password = pwd_context.hash(params['password'])
    db_user = User(username=params['username'], email=params['email'],
                   hashed_password=hashed_password)

    print(db_user)
    # Add the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to get the latest data

    return db_user  # Will return a UserResponse


@router.post("/auth/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    params = jsonable_encoder(user, exclude_none=True)

    db_user = db.query(User).filter(User.email == params['email']).first()
    if not db_user or not pwd_context.verify(params['password'], db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}
