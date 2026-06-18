"""
Authentication schemas.

Defines request and response models for authentication APIs.
"""

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """
    Schema for user login request.
    """

    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    """
    Schema for user login response.
    """

    access_token: str
    token_type: str
