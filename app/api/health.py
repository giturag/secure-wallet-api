from fastapi import APIRouter, HTTPException, status
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.api.deps import DatabaseSession 

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
def liveness():
    return {"status": "alive"}


@router.get("/ready")
def readiness(db: DatabaseSession):
    try:
        db.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable"
        )

    return {
        "status": "ready",
        "database": "available",
    }