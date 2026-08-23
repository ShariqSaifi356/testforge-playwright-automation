import logging
from pathlib import Path

FRAMEWORK_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = FRAMEWORK_DIR / "logs" 


def get_logger(test_name):

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(test_name)
    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    file_handler = logging.FileHandler(
        LOGS_DIR / f"{test_name}.log"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger