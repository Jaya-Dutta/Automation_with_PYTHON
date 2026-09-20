import logging
from pathlib import Path


def get_logger(name="api_automation"):
    """Create and return the framework logger."""

    project_root = Path(__file__).resolve().parent.parent
    log_directory = project_root / "logs"

    log_directory.mkdir(exist_ok=True)

    log_file = log_directory / "api_automation.log"

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
