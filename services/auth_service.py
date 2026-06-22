"""
Handles service operations related to authentication.
"""

from sqlalchemy.orm import Session

from mappers import user_mapper
from models.user import User


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    """
    Retrieve a user by email address.

    Args:
        db: SQLAlchemy database session.
        email: User email address.

    Returns:
        User | None: Matching user if found, otherwise None.
    """
    try:
        return user_mapper.get_user_by_email(
            db=db,
            email=email,
        )
    except Exception:
        raise
