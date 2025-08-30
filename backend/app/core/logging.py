import logging
from loguru import logger

LOG_FORMAT = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

def setup_logging():
    """
    Configure application logging with loguru.
    """
    # Remove default logger to avoid duplicates
    logger.remove()
    # Add stdout logging
    logger.add(lambda msg: print(msg, end=""), format=LOG_FORMAT, level="INFO")

    # Also connect with standard logging
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("uvicorn").handlers = []
    logging.getLogger("uvicorn.error").handlers = []
    logging.getLogger("uvicorn.access").handlers = []

    return logger

logger = setup_logging()
