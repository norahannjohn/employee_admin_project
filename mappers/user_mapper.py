"""
Handles database operations related to users.
"""

from sqlalchemy.orm import Session

from models.user import User


def get_user_by_email(
    db: Session,
    email: str,
) -> User | None:
    """
    Retrieve a user by email address.

    Args:
        db: Database session.
        email: User email.

    Returns:
        User object if found, otherwise None.
    """
    try:
        return db.query(User).filter(User.email == email).first()

    except Exception as exc:
        raise Exception("Failed to fetch user by email.") from exc


def get_user_by_id(
    db: Session,
    user_id: int,
) -> User | None:
    """
    Retrieve a user by ID.

    Args:
        db: Database session.
        user_id: User ID.

    Returns:
        User object if found, otherwise None.
    """
    try:
        return db.query(User).filter(User.id == user_id).first()

    except Exception as exc:
        raise Exception("Failed to fetch user by ID.") from exc
