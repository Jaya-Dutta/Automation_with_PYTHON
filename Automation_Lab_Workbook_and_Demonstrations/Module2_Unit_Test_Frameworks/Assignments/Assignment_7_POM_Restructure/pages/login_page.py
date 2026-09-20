import sys
from pathlib import Path

from selenium.webdriver.common.by import By


# Add Assignment 7 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from base.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the login page.

    Contains:
    - Locators
    - UI interaction methods

    Test assertions remain outside this class.
    """

    # Login page locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def enter_username(self, username):
        """Enter username into the username field."""
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        """Enter password into the password field."""
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def get_flash_message(self):
        """Return success or validation message."""
        return self.get_text(self.FLASH_MESSAGE)