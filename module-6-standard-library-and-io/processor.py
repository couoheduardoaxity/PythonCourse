import csv
import json
import logging
from datetime import datetime
from pathlib import Path


def read_csv(path: Path):
    data = []
    with path.open(mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["amount"] = float(row["amount"])
                row["date"] = datetime.fromisoformat(row["date"])
                data.append(row)
            except Exception as e:
                logging.error(f"Error parsing row {row}: {e}")
    return data


def calculate_metrics(data):
    total = sum(item["amount"] for item in data)
    count = len(data)
    avg = total / count if count else 0

    by_month = {}
    for item in data:
        month = item["date"].strftime("%Y-%m")
        by_month.setdefault(month, 0)
        by_month[month] += item["amount"]

    return {
        "total": total,
        "count": count,
        "average": avg,
        "by_month": by_month,
    }


def export_json(data, path: Path):
    path.parent.mkdir(exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, default=str)

    logging.info(f"JSON exported to {path}")
