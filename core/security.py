"""
Provides password hashing and JWT utility functions
for authentication and authorization.
"""

from jose import JWTError, jwt
from passlib.context import CryptContext

from core.configuration import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(
    password: str,
) -> str:
    """
    Hash a plain text password.

    Args:
        password: Plain text password.

    Returns:
        Hashed password.
    """
    try:
        return pwd_context.hash(password)

    except Exception as exc:
        raise Exception("Failed to hash password.") from exc


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a plain text password against its hashed value.

    Args:
        password: Plain text password.
        hashed_password: Stored hashed password.

    Returns:
        True if the password is valid, otherwise False.
    """
    try:
        return pwd_context.verify(
            password,
            hashed_password,
        )

    except Exception as exc:
        raise Exception("Failed to verify password.") from exc


def create_access_token(
    user_id: int,
    role: str,
) -> str:
    """
    Create a JWT access token.

    Args:
        user_id: Authenticated user's ID.
        role: User role.

    Returns:
        Encoded JWT access token.
    """
    try:
        payload = {
            "sub": str(user_id),
            "role": role,
        }

        token = jwt.encode(
            payload,
            settings.secret_key,
            algorithm=settings.algorithm,
        )

        return token

    except Exception as exc:
        raise Exception("Failed to create access token.") from exc


def decode_access_token(
    token: str,
) -> dict:
    """
    Decode a JWT access token.

    Args:
        token: JWT access token.

    Returns:
        Decoded JWT payload.
    """
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        return payload

    except JWTError as exc:
        raise Exception("Invalid or expired token.") from exc

    except Exception as exc:
        raise Exception("Failed to decode access token.") from exc
