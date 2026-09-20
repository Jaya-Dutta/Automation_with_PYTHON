import sys
from pathlib import Path

import pytest

# Add Module 2 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import BASE_URL
from pages.login_page import LoginPage
from utilities.csv_reader import read_csv


# Load all login test cases from CSV
DATA_FILE = PROJECT_ROOT / "test_data" / "login_data.csv"
LOGIN_DATA = read_csv(DATA_FILE)


@pytest.mark.parametrize(
    "test_data",
    LOGIN_DATA,
    ids=[row["test_case"] for row in LOGIN_DATA],
)
def test_login(driver, test_data):
    """
    Data-Driven login test.

    Each CSV row becomes a separate PyTest test case.
    """

    login_page = LoginPage(driver)

    # Open login page
    driver.get(BASE_URL)

    # Use username and password from CSV
    login_page.enter_username(test_data["username"])
    login_page.enter_password(test_data["password"])
    login_page.click_login()

    # Validate the expected success/error message
    actual_message = login_page.get_flash_message()

    assert test_data["expected_message"] in actual_message

    # Keep one successful screenshot as test evidence
    if test_data["test_case"] == "Valid Login":
        screenshot_path = (
            PROJECT_ROOT
            / "screenshots"
            / "login_test_passed.png"
        )
        driver.save_screenshot(str(screenshot_path))