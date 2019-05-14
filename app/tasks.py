import logging

logger = logging.getLogger(__name__)


async def do(param: str) -> None:
    pass  # pragma: no cover


async def log_something() -> None:
    logger.debug("debug log")
    logger.info("info log")
    logger.warning("warning log")
    logger.error("debug log")
    logger.critical("critical log")

    logger.debug("debug log 2")
    logger.error("debug error 2")
