from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):
    """
    Page Object for the login page.
    Inherits common Selenium methods from BasePage.
    """

    # Page locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def enter_username(self, username):
        """Enter username."""
        self.enter_text(self.USERNAME, username)

    def enter_password(self, password):
        """Enter password."""
        self.enter_text(self.PASSWORD, password)

    def click_login(self):
        """Click login button."""
        self.click(self.LOGIN_BUTTON)

    def get_flash_message(self):
        """Return success or validation error message."""
        return self.get_text(self.FLASH_MESSAGE)