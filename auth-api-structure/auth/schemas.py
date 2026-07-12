# auth/schemas.py
# Pydantic schemas for authentication - request/response shapes for register, login, and tokens

from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    """Schema for incoming registration data."""
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=72)
    # bcrypt has a hard 72-byte limit on passwords - max_length=72 prevents silent truncation


class UserLogin(BaseModel):
    """Schema for login credentials (used internally; actual login route uses OAuth2 form)."""
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = {"from_attributes": True}   # pydantic v2 - allows reading from ORM object


class Token(BaseModel):
    """Schema for the response after successful login."""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """Schema representing the data we decode out of a valid token."""
    username: str | None = None
