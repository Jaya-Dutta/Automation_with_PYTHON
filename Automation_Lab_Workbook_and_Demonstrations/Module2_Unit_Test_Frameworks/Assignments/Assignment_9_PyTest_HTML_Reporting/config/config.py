from pathlib import Path


# Assignment 9 project root
PROJECT_ROOT = Path(__file__).parent.parent

# Application under test
BASE_URL = "https://the-internet.herokuapp.com/login"

# HTML report location
REPORT_DIR = PROJECT_ROOT / "reports"

# Screenshot location
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"

# Create folders automatically
REPORT_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)