import sys
from pathlib import Path

import pytest


# Add Assignment 9 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import BASE_URL
from pages.login_page import LoginPage


class TestLogin:
    """
    Login tests for Assignment 9.

    Browser setup and teardown are handled
    automatically by conftest.py.
    """

    def test_valid_login(self, driver):
        """Verify successful login."""

        login_page = LoginPage(driver)

        # Open login page
        driver.get(BASE_URL)

        # Perform login
        login_page.enter_username("tomsmith")
        login_page.enter_password("SuperSecretPassword!")
        login_page.click_login()

        # Assertion for intentional failure testing
        actual_message = login_page.get_flash_message()
        assert "You logged into a secure area!" in actual_message
        #assert "THIS SHOULD FAIL" in actual_message