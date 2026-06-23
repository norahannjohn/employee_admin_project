"""
Defines authentication API endpoints.
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
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

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        ) from exc

    except PermissionError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed.",
        ) from exc
