from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from core.db import get_db
from core.dependencies import get_current_admin
from handlers import asset_handler
from models.user import User
from schema.asset_schema import (
    AssetTypeResponse,
    CreateAssetTypeRequest,
    UpdateAssetTypeRequest,
)

router = APIRouter(
    prefix="/asset-types",
    tags=["Asset Types"],
)


@router.post(
    "",
    response_model=AssetTypeResponse,
)
def create_asset(
    asset_data: CreateAssetTypeRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Create a new asset type.

    Args:
        asset_data: Asset type details provided in the request body.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Newly created asset type.
    """
    try:
        return asset_handler.create_asset(
            db=db,
            asset_data=asset_data,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        ) from exc


@router.get(
    "",
    response_model=list[AssetTypeResponse],
)
def get_all_assets(
    db: Session = Depends(get_db),
):
    """
    Retrieve all asset types.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list[AssetTypeResponse]: List of all asset types.
    """
    try:
        return asset_handler.get_all_assets(
            db=db,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve asset types.",
        ) from exc


@router.patch(
    "/{asset_id}",
    response_model=AssetTypeResponse,
)
def update_asset(
    asset_id: int,
    asset_data: UpdateAssetTypeRequest,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Update an existing asset type.

    Args:
        asset_id: Unique asset type identifier.
        asset_data: Updated asset type information.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Updated asset type.
    """
    try:
        return asset_handler.update_asset(
            db=db,
            asset_id=asset_id,
            asset_data=asset_data,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc


@router.delete(
    "/{asset_id}",
    response_model=AssetTypeResponse,
)
def deactivate_asset(
    asset_id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin),
):
    """
    Deactivate an existing asset type.

    Args:
        asset_id: Unique asset type identifier.
        db: SQLAlchemy database session.

    Returns:
        AssetTypeResponse: Deactivated asset type.
    """
    try:
        return asset_handler.deactivate_asset(
            db=db,
            asset_id=asset_id,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        ) from exc
