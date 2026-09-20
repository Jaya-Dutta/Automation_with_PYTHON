import csv
from pathlib import Path


def read_csv(file_path):
    """
    Read CSV test data and return each row as a dictionary.
    """

    file_path = Path(file_path)

    with file_path.open(
        mode="r",
        encoding="utf-8",
        newline=""
    ) as file:
        return list(csv.DictReader(file))