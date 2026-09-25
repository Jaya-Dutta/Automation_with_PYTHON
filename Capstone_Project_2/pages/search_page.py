from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class SearchPage(BasePage):

    search_box = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
    searched_products = (By.XPATH, "//h2[contains(text(),'Searched Products')]")
    add_to_cart_modal = (
        By.XPATH,
        "//div[contains(@class,'modal-content')]"
        "[.//*[contains(normalize-space(),'Added!')]]"
    )
    view_cart_modal = (
        By.XPATH,
        "//div[contains(@class,'modal-content')]"
        "//a[contains(@href,'/view_cart')]"
    )

    def search_product(self, product):
        self.enter_text(self.search_box, product)
        self.click(self.search_button)

    def is_search_result_visible(self):
        return self.wait_for_visible(self.searched_products).is_displayed()

    def add_product_to_cart(self, product):
        locator = (
            By.XPATH,
            f"//p[normalize-space()='{product}']"
            "/following-sibling::a[contains(@class,'add-to-cart')]"
        )

        element = self.wait_for_visible(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

        WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(self.add_to_cart_modal)
        )

    def open_cart_from_modal(self):
        self.click(self.view_cart_modal)