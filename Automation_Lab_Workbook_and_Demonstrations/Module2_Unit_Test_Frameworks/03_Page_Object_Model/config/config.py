from pathlib import Path


# Project root: 03_Page_Object_Model
PROJECT_ROOT = Path(__file__).parent.parent

# Application under test
BASE_URL = "https://the-internet.herokuapp.com/login"

# Explicit wait timeout in seconds
WAIT_TIMEOUT = 10

# Screenshot folder
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"

# Create screenshot folder if it does not exist
SCREENSHOT_DIR.mkdir(exist_ok=True)