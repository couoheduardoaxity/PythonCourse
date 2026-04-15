import logging
from pathlib import Path


def setup_logger():
    log_path = Path("logs/app.log")
    log_path.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_path), logging.StreamHandler()],
    )
