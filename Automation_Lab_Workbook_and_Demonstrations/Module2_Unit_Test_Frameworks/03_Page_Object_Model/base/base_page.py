from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Common Selenium operations used by all Page classes.
    """

    def __init__(self, driver):
        # Store the browser driver for reuse in page classes
        self.driver = driver

        # Create an explicit wait with a 10-second timeout
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Wait until an element is visible and return it."""
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator):
        """Wait for an element and click it."""
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def enter_text(self, locator, text):
        """Clear an input field and enter text."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Return visible text from an element."""
        return self.find_element(locator).text

    def get_attribute(self, locator, attribute):
        """Return an element attribute value."""
        return self.find_element(locator).get_attribute(attribute)