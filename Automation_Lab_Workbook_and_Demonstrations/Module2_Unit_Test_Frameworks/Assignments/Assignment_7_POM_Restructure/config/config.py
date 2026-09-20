from pathlib import Path


# Assignment 7 project root
PROJECT_ROOT = Path(__file__).parent.parent

# Application under test
BASE_URL = "https://the-internet.herokuapp.com/login"

# Explicit wait timeout
WAIT_TIMEOUT = 10

# Screenshot and report folders
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
REPORT_DIR = PROJECT_ROOT / "reports"

# Create folders if they do not exist
SCREENSHOT_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)