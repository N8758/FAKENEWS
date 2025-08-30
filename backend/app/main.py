from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import routes_health, routes_predict
from app.core.config import settings
from app.core.logging import logger

def create_app() -> FastAPI:
    """
    Application factory to create FastAPI app.
    """
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG,
        description="🚀 Fake News Detection API using DistilBERT"
    )

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[origin.strip() for origin in settings.ALLOWED_ORIGINS.split(",")],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Register routers
    app.include_router(routes_health.router, prefix="/api/v1")
    app.include_router(routes_predict.router, prefix="/api/v1")

    logger.success("✅ FastAPI app initialized successfully")

    return app


# Create app instance
app = create_app()
