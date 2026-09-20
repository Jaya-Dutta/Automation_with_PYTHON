import sys
from pathlib import Path

import pytest


# Add Assignment 7 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import BASE_URL
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """
    Create browser before the test
    and close it after the test.
    """
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


class TestLogin:
    """
    Login test class.

    Assertions are kept here.
    Locators and UI actions are handled by LoginPage.
    """

    def test_valid_login(self, driver):
        """Verify successful login using Page Object Model."""

        login_page = LoginPage(driver)

        # Open login page
        driver.get(BASE_URL)

        # Perform login through Page Object methods
        login_page.enter_username("tomsmith")
        login_page.enter_password("SuperSecretPassword!")
        login_page.click_login()

        # Assertion belongs to the test layer
        actual_message = login_page.get_flash_message()

        assert "You logged into a secure area!" in actual_message

        # Save successful test evidence
        screenshot_path = (
            PROJECT_ROOT
            / "screenshots"
            / "assignment_7_login_passed.png"
        )

        driver.save_screenshot(str(screenshot_path))