"""
Handles authentication-related business logic.
"""

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
        ValueError: If the email does not exist or the password is incorrect.
        PermissionError: If the user account is inactive.
    """
    try:
        user = auth_service.get_user_by_email(
            db=db,
            email=login_request.email,
        )

        if user is None:
            raise ValueError(
                "Invalid email or password.",
            )

        if not user.is_active:
            raise PermissionError(
                "User account is inactive.",
            )

        if not verify_password(
            login_request.password,
            user.password_hash,
        ):
            raise ValueError(
                "Invalid email or password.",
            )

        access_token = create_access_token(
            user_id=user.id,
            role=user.role.value,
        )

        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
        )

    except Exception:
        raise
