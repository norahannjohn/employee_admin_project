"""
Defines asset request API endpoints.
"""

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from core.db import get_db
from core.dependencies import get_current_user
from handlers import request_handler
from models.user import User
from schema.request_schema import (
    CreateRequest,
    RequestResponse,
)

router = APIRouter(
    prefix="/requests",
    tags=["Asset Requests"],
)


@router.post(
    "",
    response_model=RequestResponse,
)
def create_request(
    request_data: CreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Create a new asset request.

    Args:
        request_data: Asset request details.
        db: SQLAlchemy database session.
        current_user: Authenticated user.

    Returns:
        RequestResponse: Newly created asset request.
    """
    try:
        return request_handler.create_request(
            db=db,
            current_user=current_user,
            request_data=request_data,
        )

    except ValueError as exc:
        message = str(exc)

        if message == "Asset type not found.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from exc

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create request.",
        ) from exc


@router.get(
    "/me",
    response_model=list[RequestResponse],
)
def get_my_requests(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> list[RequestResponse]:
    """
    Retrieve all asset requests created by the authenticated user.
    """
    try:
        return request_handler.get_my_requests(
            db=db,
            current_user=current_user,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve requests.",
        ) from exc


@router.get(
    "/{request_id}",
    response_model=RequestResponse,
)
def get_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Retrieve an asset request by its ID.
    """
    try:
        return request_handler.get_request(
            db=db,
            request_id=request_id,
            current_user=current_user,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
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
            detail="Failed to retrieve request.",
        ) from exc


@router.patch(
    "/{request_id}/cancel",
    response_model=RequestResponse,
)
def cancel_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> RequestResponse:
    """
    Cancel a pending asset request.
    """
    try:
        return request_handler.cancel_request(
            db=db,
            request_id=request_id,
            current_user=current_user,
        )

    except ValueError as exc:
        message = str(exc)

        if message == "Request not found.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from exc

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from exc

    except PermissionError as exc:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to cancel request.",
        ) from exc
