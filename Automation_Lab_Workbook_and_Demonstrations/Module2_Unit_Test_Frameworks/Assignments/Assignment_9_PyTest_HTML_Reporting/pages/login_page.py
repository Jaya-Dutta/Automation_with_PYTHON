from selenium.webdriver.common.by import By


class LoginPage:
    """
    Page Object for the login page.
    """

    # Login page locators
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        """Enter username."""
        element = self.driver.find_element(*self.USERNAME)
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        """Enter password."""
        element = self.driver.find_element(*self.PASSWORD)
        element.clear()
        element.send_keys(password)

    def click_login(self):
        """Click login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_flash_message(self):
        """Return login result message."""
        return self.driver.find_element(*self.FLASH_MESSAGE).text