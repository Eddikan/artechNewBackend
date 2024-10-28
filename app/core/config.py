from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # DATABASE_URL: str = "postgresql://postgres.lgrxvzsyzsnxdsvijonh:moneymistressmagiC1#@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
    DATABASE_URL: str = "sqlite:///./test.db"
    JWT_SECRET_KEY: str = "your_jwt_secret_key"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
