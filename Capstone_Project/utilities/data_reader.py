import json
from pathlib import Path


class DataReader:
    """Read JSON test data from the project test_data directory."""

    @staticmethod
    def read_json(filename):
        project_root = Path(__file__).resolve().parent.parent
        file_path = project_root / "test_data" / filename

        with open(file_path, "r", encoding="utf-8-sig") as file:
            return json.load(file)
