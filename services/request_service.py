"""
Asset request service.

Handles service operations related to asset requests.
"""

from sqlalchemy.orm import Session

from mappers import request_mapper
from models.asset_request import AssetRequest, RequestStatus


def create_request(
    db: Session,
    asset_request: AssetRequest,
) -> AssetRequest:
    """
    Create a new asset request.

    Args:
        db: SQLAlchemy database session.
        asset_request: Asset request object to be created.

    Returns:
        AssetRequest: Newly created asset request.
    """
    try:
        return request_mapper.create_request(
            db=db,
            asset_request=asset_request,
        )
    except Exception:
        raise


def get_request_by_id(
    db: Session,
    request_id: int,
) -> AssetRequest | None:
    """
    Retrieve an asset request by its ID.

    Args:
        db: SQLAlchemy database session.
        request_id: Unique asset request identifier.

    Returns:
        AssetRequest | None: Matching asset request if found, otherwise None.
    """
    try:
        return request_mapper.get_request_by_id(
            db=db,
            request_id=request_id,
        )
    except Exception:
        raise


def get_user_requests(
    db: Session,
    user_id: int,
) -> list[AssetRequest]:
    """
    Retrieve all asset requests created by a user.

    Args:
        db: SQLAlchemy database session.
        user_id: Unique user identifier.

    Returns:
        list[AssetRequest]: List of asset requests created by the user.
    """
    try:
        return request_mapper.get_user_requests(
            db=db,
            user_id=user_id,
        )
    except Exception:
        raise


def get_all_requests(
    db: Session,
    status: RequestStatus | None = None,
) -> list[AssetRequest]:
    """
    Retrieve all asset requests.

    Args:
        db: SQLAlchemy database session.
        status: Optional request status filter.

    Returns:
        list[AssetRequest]: List of matching asset requests.
    """
    try:
        return request_mapper.get_all_requests(
            db=db,
            status=status,
        )
    except Exception:
        raise


def update_request(
    db: Session,
    asset_request: AssetRequest,
) -> AssetRequest:
    """
    Update an existing asset request.

    Args:
        db: SQLAlchemy database session.
        asset_request: Asset request object with updated values.

    Returns:
        AssetRequest: Updated asset request.
    """
    try:
        return request_mapper.update_request(
            db=db,
            asset_request=asset_request,
        )
    except Exception:
        raise
