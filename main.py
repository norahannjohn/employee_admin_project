"""
Initializes the FastAPI application and registers API routers.
"""

from fastapi import FastAPI

from routers.admin_router import router as admin_router
from routers.asset_type_router import router as asset_router
from routers.auth_router import router as auth_router
from routers.request_router import router as request_router

app = FastAPI(
    title="Employee Asset Management API",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(asset_router)
app.include_router(request_router)
app.include_router(admin_router)


@app.get("/")
def health_check() -> dict[str, str]:
    """
    Health check endpoint.

    Returns:
        dict[str, str]: API status.
    """
    try:
        return {"message": "Employee Asset Management API is running."}

    except Exception:
        raise
