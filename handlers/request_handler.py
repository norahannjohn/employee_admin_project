"""
Handles business logic related to asset requests.
"""

from sqlalchemy.orm import Session

from models.asset_request import (
    AssetRequest,
    RequestStatus,
)
from models.user import User
from schema.request_schema import CreateRequest
from services import (
    asset_service,
    request_service,
)


def create_request(
    db: Session,
    current_user: User,
    request_data: CreateRequest,
) -> AssetRequest:
    """
    Create a new asset request.

    Args:
        db: SQLAlchemy database session.
        current_user: Authenticated user.
        request_data: Asset request details.

    Returns:
        AssetRequest: Newly created asset request.

    Raises:
        ValueError: If the asset type does not exist or is inactive.
    """
    try:
        asset = asset_service.get_asset_by_id(
            db=db,
            asset_id=request_data.asset_type_id,
        )

        if asset is None:
            raise ValueError(
                "Asset type not found.",
            )

        if not asset.is_active:
            raise ValueError(
                "Asset type is inactive.",
            )

        asset_request = AssetRequest(
            user_id=current_user.id,
            asset_type_id=request_data.asset_type_id,
            reason=request_data.reason,
            status=RequestStatus.PENDING,
        )

        return request_service.create_request(
            db=db,
            asset_request=asset_request,
        )

    except Exception:
        raise


def get_my_requests(
    db: Session,
    current_user: User,
) -> list[AssetRequest]:
    """
    Retrieve all asset requests created by the current user.
    """
    try:
        return request_service.get_user_requests(
            db=db,
            user_id=current_user.id,
        )

    except Exception:
        raise


def get_request(
    db: Session,
    request_id: int,
    current_user: User,
) -> AssetRequest:
    """
    Retrieve an asset request by its ID.

    Raises:
        ValueError: If the request does not exist.
        PermissionError: If the user is not authorized.
    """
    try:
        asset_request = request_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if asset_request is None:
            raise ValueError(
                "Request not found.",
            )

        if asset_request.user_id != current_user.id:
            raise PermissionError(
                "Access denied.",
            )

        return asset_request

    except Exception:
        raise


def cancel_request(
    db: Session,
    request_id: int,
    current_user: User,
) -> AssetRequest:
    """
    Cancel a pending asset request.

    Raises:
        ValueError: If request does not exist or is not pending.
        PermissionError: If request belongs to another user.
    """
    try:
        asset_request = request_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if asset_request is None:
            raise ValueError(
                "Request not found.",
            )

        if asset_request.user_id != current_user.id:
            raise PermissionError(
                "You can only cancel your own requests.",
            )

        if asset_request.status != RequestStatus.PENDING:
            raise ValueError(
                "Only pending requests can be cancelled.",
            )

        asset_request.status = RequestStatus.CANCELLED

        return request_service.update_request(
            db=db,
            asset_request=asset_request,
        )

    except Exception:
        raise


def approve_request(
    db: Session,
    request_id: int,
    admin_comment: str,
) -> AssetRequest:
    """
    Approve an asset request.
    """
    try:
        asset_request = request_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if asset_request is None:
            raise ValueError(
                "Request not found.",
            )

        if asset_request.status != RequestStatus.PENDING:
            raise ValueError(
                "Only pending requests can be approved.",
            )

        asset_request.status = RequestStatus.APPROVED
        asset_request.admin_comment = admin_comment

        return request_service.update_request(
            db=db,
            asset_request=asset_request,
        )

    except Exception:
        raise


def reject_request(
    db: Session,
    request_id: int,
    admin_comment: str,
) -> AssetRequest:
    """
    Reject an asset request.
    """
    try:
        asset_request = request_service.get_request_by_id(
            db=db,
            request_id=request_id,
        )

        if asset_request is None:
            raise ValueError(
                "Request not found.",
            )

        if asset_request.status != RequestStatus.PENDING:
            raise ValueError(
                "Only pending requests can be rejected.",
            )

        asset_request.status = RequestStatus.REJECTED
        asset_request.admin_comment = admin_comment

        return request_service.update_request(
            db=db,
            asset_request=asset_request,
        )

    except Exception:
        raise
