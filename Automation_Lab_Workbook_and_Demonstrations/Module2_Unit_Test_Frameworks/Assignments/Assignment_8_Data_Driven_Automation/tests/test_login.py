import sys
from pathlib import Path

import pytest


# Add Assignment 8 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import BASE_URL
from pages.login_page import LoginPage
from utilities.csv_reader import read_csv


# Load login test data from CSV
DATA_FILE = PROJECT_ROOT / "test_data" / "login_data.csv"
LOGIN_DATA = read_csv(DATA_FILE)


@pytest.fixture
def driver():
    """
    Create browser before each test
    and close it after the test.
    """
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.mark.parametrize(
    "test_data",
    LOGIN_DATA,
    ids=[row["test_case"] for row in LOGIN_DATA],
)
def test_login_with_csv_data(driver, test_data):
    """
    Data-Driven login test.

    Each CSV row is executed as a separate PyTest test case.
    """

    login_page = LoginPage(driver)

    # Open login page
    driver.get(BASE_URL)

    # Enter test data from CSV
    login_page.enter_username(test_data["username"])
    login_page.enter_password(test_data["password"])
    login_page.click_login()

    # Validate expected success/error message
    actual_message = login_page.get_flash_message()

    assert test_data["expected_message"] in actual_message