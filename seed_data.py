"""
Database seed script.

Populates the database with initial users,
asset types, and asset requests.
"""

from sqlalchemy.orm import Session

from core.db import SessionLocal
from core.security import hash_password

from models.asset_request import (
    AssetRequest,
    RequestStatus,
)
from models.asset_type import AssetType
from models.user import User, UserRole


def seed_database() -> None:
    """
    Seed the database with initial data.

    Creates default users, asset types,
    and asset requests if they do not already exist.
    """
    db: Session = SessionLocal()

    try:
        print("Starting database seeding...")

        existing_admin = (
            db.query(User).filter(User.email == "admin@company.com").first()
        )

        if existing_admin is None:
            admin = User(
                name="Admin User",
                email="admin@company.com",
                password_hash=hash_password("admin123"),
                role=UserRole.ADMIN,
                is_active=True,
            )

            db.add(admin)
            print("Admin user created.")

        else:
            admin = existing_admin
            print("Admin user already exists.")

        existing_john = db.query(User).filter(User.email == "john@company.com").first()

        if existing_john is None:
            john = User(
                name="John Doe",
                email="john@company.com",
                password_hash=hash_password("john123"),
                role=UserRole.EMPLOYEE,
                is_active=True,
            )

            db.add(john)
            print("John created.")

        else:
            john = existing_john
            print("John already exists.")

        existing_emma = db.query(User).filter(User.email == "emma@company.com").first()

        if existing_emma is None:
            emma = User(
                name="Emma Smith",
                email="emma@company.com",
                password_hash=hash_password("emma123"),
                role=UserRole.EMPLOYEE,
                is_active=True,
            )

            db.add(emma)
            print("Emma created.")

        else:
            emma = existing_emma
            print("Emma already exists.")

        asset_types = [
            {
                "name": "Laptop",
                "description": "Company-issued laptop.",
            },
            {
                "name": "Monitor",
                "description": "External monitor.",
            },
            {
                "name": "Keyboard",
                "description": "Mechanical keyboard.",
            },
            {
                "name": "Mouse",
                "description": "Wireless mouse.",
            },
        ]

        for asset_data in asset_types:
            existing_asset = (
                db.query(AssetType)
                .filter(
                    AssetType.name == asset_data["name"],
                )
                .first()
            )

            if existing_asset is None:
                asset = AssetType(
                    name=asset_data["name"],
                    description=asset_data["description"],
                    is_active=True,
                )

                db.add(asset)

                print(
                    f"{asset.name} asset type created.",
                )

            else:
                print(
                    f"{existing_asset.name} already exists.",
                )

        db.flush()

        # Retrieve Asset Types

        assets = {asset.name: asset for asset in db.query(AssetType).all()}

        # Create Sample Requests

        existing_request = (
            db.query(AssetRequest)
            .filter(
                AssetRequest.user_id == john.id,
                AssetRequest.asset_type_id == assets["Laptop"].id,
            )
            .first()
        )

        if existing_request is None:
            requests = [
                AssetRequest(
                    user_id=john.id,
                    asset_type_id=assets["Laptop"].id,
                    reason="Need a laptop for development work.",
                    status=RequestStatus.PENDING,
                ),
                AssetRequest(
                    user_id=emma.id,
                    asset_type_id=assets["Monitor"].id,
                    reason="Need a second monitor for productivity.",
                    status=RequestStatus.APPROVED,
                    admin_comment="Approved.",
                ),
                AssetRequest(
                    user_id=john.id,
                    asset_type_id=assets["Mouse"].id,
                    reason="Current mouse is damaged.",
                    status=RequestStatus.REJECTED,
                    admin_comment="Budget unavailable.",
                ),
                AssetRequest(
                    user_id=emma.id,
                    asset_type_id=assets["Keyboard"].id,
                    reason="Need an ergonomic keyboard.",
                    status=RequestStatus.CANCELLED,
                ),
            ]

            db.add_all(requests)

            print("Sample asset requests created.")

        else:
            print("Asset requests already exist.")

        db.commit()

        print("Database seeded successfully.")

    except Exception as exc:
        db.rollback()
        raise Exception("Failed to seed database.") from exc

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
