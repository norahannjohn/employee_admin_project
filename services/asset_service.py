from sqlalchemy.orm import Session

from mappers import asset_mapper
from models.asset_type import AssetType


def create_asset(
    db: Session,
    asset: AssetType,
) -> AssetType:
    """
    Create a new asset type.

    Args:
        db: SQLAlchemy database session.
        asset: Asset type object to be created.

    Returns:
        AssetType: Newly created asset type.
    """
    try:
        return asset_mapper.create_asset(
            db=db,
            asset=asset,
        )
    except Exception:
        raise


def get_asset_by_id(
    db: Session,
    asset_id: int,
) -> AssetType | None:
    """
    Retrieve an asset type by its ID.

    Args:
        db: SQLAlchemy database session.
        asset_id: Unique asset type identifier.

    Returns:
        AssetType | None: Matching asset type if found, otherwise None.
    """
    try:
        return asset_mapper.get_asset_by_id(
            db=db,
            asset_id=asset_id,
        )
    except Exception:
        raise


def get_asset_by_name(
    db: Session,
    name: str,
) -> AssetType | None:
    """
    Retrieve an asset type by its name.

    Args:
        db: SQLAlchemy database session.
        name: Name of the asset type.

    Returns:
        AssetType | None: Matching asset type if found, otherwise None.
    """
    try:
        return asset_mapper.get_asset_by_name(
            db=db,
            name=name,
        )
    except Exception:
        raise


def get_all_assets(
    db: Session,
) -> list[AssetType]:
    """
    Retrieve all asset types.

    Args:
        db: SQLAlchemy database session.

    Returns:
        list[AssetType]: List of all asset types.
    """
    try:
        return asset_mapper.get_all_assets(
            db=db,
        )
    except Exception:
        raise


def update_asset(
    db: Session,
    asset: AssetType,
) -> AssetType:
    """
    Update an existing asset type.

    Args:
        db: SQLAlchemy database session.
        asset: Asset type object with updated values.

    Returns:
        AssetType: Updated asset type.
    """
    try:
        return asset_mapper.update_asset(
            db=db,
            asset=asset,
        )
    except Exception:
        raise


def deactivate_asset(
    db: Session,
    asset: AssetType,
) -> AssetType:
    """
    Deactivate an asset type.

    Args:
        db: SQLAlchemy database session.
        asset: Asset type to be deactivated.

    Returns:
        AssetType: Deactivated asset type.
    """
    try:
        return asset_mapper.deactivate_asset(
            db=db,
            asset=asset,
        )
    except Exception:
        raise
