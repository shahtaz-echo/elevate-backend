from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: str
    last_name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    bio: Optional[str] = None
    designation: Optional[str] = None
    image: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None 

    class Config:
        from_attributes = True

class TokenInList(BaseModel):
    access_token: str
    refresh_token: str

class LoginPayload(BaseModel):
    userOrEmail: str
    password: str
    
class CreatedNewUserInList(BaseModel):
    user: User
    access_token: str
    refresh_token: str

    class Config:
        from_attributes = True

class UserUpdateInPayload(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    designation: Optional[str] = None
    image: Optional[str] = None

    class Config:
        extra = "forbid"
