import logging

from app.core.config import settings

def setup_logging() -> None:
    """Configure the root logger once at startup, using the level from settings."""
    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    )