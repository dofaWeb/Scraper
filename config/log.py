import logging

# Basic logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="scraper.log",  # Log output to this file
    filemode="a",  # Append to file
)

# Get the logger
logger = logging.getLogger(__name__)


def log_message(message):
    logger.info(message)


def log_error(message, error=None):
    logger.error(message)
    if error:
        logger.exception(error)