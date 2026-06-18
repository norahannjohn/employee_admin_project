from sqlalchemy.orm import Session

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
        db.add(asset)
        db.commit()
        db.refresh(asset)
        return asset
    except Exception:
        db.rollback()
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
        return db.query(AssetType).filter(AssetType.id == asset_id).first()
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
        return db.query(AssetType).filter(AssetType.name == name).first()
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
        return db.query(AssetType).all()
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
        db.commit()
        db.refresh(asset)
        return asset
    except Exception:
        db.rollback()
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
        asset.is_active = False
        db.commit()
        db.refresh(asset)
        return asset
    except Exception:
        db.rollback()
        raise
