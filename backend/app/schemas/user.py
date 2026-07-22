from pydantic import BaseModel
from pydantic import EmailStr

from app.models.enums import UserRole


class UserCreate(BaseModel):

    full_name: str

    email: EmailStr

    password: str

    role: UserRole


class UserResponse(BaseModel):

    id: str

    full_name: str

    email: EmailStr

    role: UserRole

    class Config:
        from_attributes = True