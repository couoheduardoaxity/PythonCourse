import logging
from pathlib import Path

from logger_config import setup_logger
from processor import calculate_metrics, export_json, read_csv


def main():
    setup_logger()

    input_path = Path("data/input.csv")
    output_path = Path("output/result.json")

    logging.info("Starting processing")

    if not input_path.exists():
        logging.error("Input file does not exist")
        return

    data = read_csv(input_path)
    metrics = calculate_metrics(data)
    export_json(metrics, output_path)

    logging.info("Process finished successfully")


if __name__ == "__main__":
    main()
