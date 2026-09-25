from configparser import ConfigParser
from pathlib import Path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


config_file = Path(__file__).resolve().parent.parent / "config" / "config.ini"


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        config = ConfigParser()
        config.read(config_file)
        self.timeout = config.getint("wait", "timeout")

    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_click(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
    def click(self, locator):
        element = self.wait_for_click(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def open_url(self, url):
        self.driver.get(url)