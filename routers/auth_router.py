"""
Authentication router.

Defines authentication API endpoints.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from handlers.auth_handler import login
from schema.auth_schema import (
    LoginRequest,
    LoginResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login_user(
    login_request: LoginRequest,
    db: Session = Depends(get_db),
) -> LoginResponse:
    """
    Authenticate a user and return a JWT access token.

    Args:
        login_request: User login credentials.
        db: SQLAlchemy database session.

    Returns:
        LoginResponse: JWT access token response.
    """
    try:
        return login(
            db=db,
            login_request=login_request,
        )

    except Exception:
        raise
