"""
Asset request mapper.

Handles database operations related to asset requests.
"""

from sqlalchemy.orm import Session

from models.asset_request import (
    AssetRequest,
    RequestStatus,
)


def create_request(
    db: Session,
    asset_request: AssetRequest,
) -> AssetRequest:
    """
    Create a new asset request.

    Args:
        db: Database session.
        asset_request: Asset request object.

    Returns:
        Newly created asset request.
    """
    try:
        db.add(asset_request)
        db.commit()
        db.refresh(asset_request)

        return asset_request

    except Exception as exc:
        db.rollback()
        raise Exception("Failed to create asset request.") from exc


def get_request_by_id(
    db: Session,
    request_id: int,
) -> AssetRequest | None:
    """
    Retrieve an asset request by its ID.

    Args:
        db: Database session.
        request_id: Asset request ID.

    Returns:
        Asset request if found, otherwise None.
    """
    try:
        return db.query(AssetRequest).filter(AssetRequest.id == request_id).first()

    except Exception as exc:
        raise Exception(f"Failed to fetch request with ID: {request_id}") from exc


def get_user_requests(
    db: Session,
    user_id: int,
) -> list[AssetRequest]:
    """
    Retrieve all asset requests created by a user.

    Args:
        db: Database session.
        user_id: User ID.

    Returns:
        List of asset requests.
    """
    try:
        return (
            db.query(AssetRequest)
            .filter(AssetRequest.user_id == user_id)
            .order_by(AssetRequest.created_at.desc())
            .all()
        )

    except Exception as exc:
        raise Exception(f"Failed to fetch requests for user ID: {user_id}") from exc


def get_all_requests(
    db: Session,
    status: RequestStatus | None = None,
) -> list[AssetRequest]:
    """
    Retrieve all asset requests.

    Args:
        db: Database session.
        status: Optional request status filter.

    Returns:
        List of asset requests.
    """
    try:
        query = db.query(AssetRequest)

        if status:
            query = query.filter(
                AssetRequest.status == status,
            )

        return query.order_by(AssetRequest.created_at.desc()).all()

    except Exception as exc:
        raise Exception("Failed to fetch asset requests.") from exc


def update_request(
    db: Session,
    asset_request: AssetRequest,
) -> AssetRequest:
    """
    Update an asset request.

    Args:
        db: Database session.
        asset_request: Asset request object.

    Returns:
        Updated asset request.
    """
    try:
        db.commit()
        db.refresh(asset_request)

        return asset_request

    except Exception as exc:
        db.rollback()
        raise Exception("Failed to update asset request.") from exc
