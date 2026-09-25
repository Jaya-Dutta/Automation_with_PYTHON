import csv
from pathlib import Path


def read_csv(file_name):
    file_path = Path(__file__).resolve().parent.parent / "test_data" / file_name

    with open(file_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))