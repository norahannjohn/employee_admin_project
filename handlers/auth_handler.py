"""
Authentication handler.

Handles authentication-related business logic.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.security import (
    create_access_token,
    verify_password,
)
from schema.auth_schema import (
    LoginRequest,
    LoginResponse,
)
from services import auth_service


def login(
    db: Session,
    login_request: LoginRequest,
) -> LoginResponse:
    """
    Authenticate a user.

    Args:
        db: SQLAlchemy database session.
        login_request: User login credentials.

    Returns:
        LoginResponse: JWT access token response.

    Raises:
        HTTPException: If the email does not exist, the account is inactive,
            or the password is incorrect.
    """
    try:
        user = auth_service.get_user_by_email(
            db=db,
            email=login_request.email,
        )

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive.",
            )

        if not verify_password(
            login_request.password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        access_token = create_access_token(
            user_id=user.id,
            role=user.role.value,
        )

        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
        )

    except HTTPException:
        raise

    except Exception:
        raise
