from pydantic import BaseModel

# Schema for creating a user
class UserCreate(BaseModel):
    name: str
    email: str

# Schema for reading (output) a user with ID
class UserRead(UserCreate):
    id: int

    class Config:
        orm_mode = True
