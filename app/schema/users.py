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
    update_at: Optional[datetime] = None 

    class Config:
        from_attributes = True


class UserInList(BaseModel):
    first_name: str
    last_name: str
    email: str
    bio: str
    image: str
    designation: str

class TokenInList(BaseModel):
    access_token: str
    refresh_token: str

class LoginPayload(BaseModel):
    userOrEmail: str
    password: str

class RegisterPayloadInList(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    username: str
    
class CreatedNewUserInList(BaseModel):
    user: User
    access_token: str
    refresh_token: str

    class Config:
        from_attributes = True
