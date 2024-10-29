from pydantic import BaseModel

class SubscriberCreate(BaseModel):
    email: str

class SubscriberOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True
