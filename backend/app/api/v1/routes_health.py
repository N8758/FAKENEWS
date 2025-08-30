from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health", tags=["health"])
async def health_check():
    """
    Simple health check endpoint.
    Returns status and server timestamp.
    """
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }
