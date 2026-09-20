import sys
from pathlib import Path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Add Assignment 7 root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.config import WAIT_TIMEOUT


class BasePage:
    """
    Common Selenium operations shared by all Page Objects.
    """

    def __init__(self, driver):
        # Store browser driver
        self.driver = driver

        # Create reusable explicit wait
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def find_element(self, locator):
        """Wait for an element to become visible."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Wait until an element is clickable and click it."""
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        """Clear an input and enter text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return visible text from an element."""
        return self.find_element(locator).text