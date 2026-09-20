from pathlib import Path
import yaml


class ConfigReader:
    """Load and provide access to framework configuration."""

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "config.yaml"

        with open(config_path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get(self, section, key):
        """Return a configuration value from a section."""
        return self.config[section][key]
