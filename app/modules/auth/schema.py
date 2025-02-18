from pydantic import BaseModel

class UserInList(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: str
    designation: str

class TokenInList(BaseModel):
    access_token: str
    refresh_token: str
