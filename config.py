import os
import logging
from logging.handlers import RotatingFileHandler

PLOTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plots")
log_file = "app.log"
log_level = logging.DEBUG

log_format = "%(asctime)s - %(levelname)s - %(message)s"
log_datefmt = "%Y-%m-%d %H:%M"

logger = logging.getLogger("arbor")
if not logger.hasHandlers():
    logger.setLevel(log_level)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(log_format, datefmt=log_datefmt))

    file_handler = RotatingFileHandler(
        log_file, maxBytes=10 * 1024 * 1024, backupCount=5
    )
    file_handler.setLevel(log_level)
    file_handler.setFormatter(logging.Formatter(log_format, datefmt=log_datefmt))

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
