"""
Admin service.

Handles admin operations related to asset requests.
"""

from sqlalchemy.orm import Session

from models.asset_request import AssetRequest
from services import request_service


def get_all_requests(
    db: Session,
):
    """
    Retrieve all asset requests.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list[AssetRequest]: List of asset requests.
    """
    try:
        return request_service.get_all_requests(
            db=db,
        )
    except Exception:
        raise


def get_request_by_id(
    db: Session,
    request_id: int,
) -> AssetRequest | None:
    """
    Retrieve an asset request by ID.

    Args:
        db: SQLAlchemy database session.
        request_id: Asset request identifier.

    Returns:
        AssetRequest | None: Matching asset request if found.
    """
    try:
        return request_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )
    except Exception:
        raise


def update_request(
    db: Session,
    asset_request: AssetRequest,
) -> AssetRequest:
    """
    Update an asset request.

    Args:
        db: SQLAlchemy database session.
        asset_request: Updated asset request object.

    Returns:
        AssetRequest: Updated asset request.
    """
    try:
        return request_service.update_request(
            db=db,
            asset_request=asset_request,
        )
    except Exception:
        raise
