from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    cart_link = (By.CSS_SELECTOR, "a[href='/view_cart']")
    cart_heading = (
        By.XPATH,
        "//li[contains(@class,'active') and contains(text(),'Shopping Cart')]"
    )
    product_name = (
        By.XPATH,
        "//td[contains(@class,'cart_description')]//a"
    )

    def open_cart(self):
        self.click(self.cart_link)

    def is_cart_visible(self):
        return self.wait_for_visible(self.cart_heading).is_displayed()

    def is_product_visible(self, product):
        locator = (
            By.XPATH,
            f"//td[contains(@class,'cart_description')]//a[normalize-space()='{product}']"
        )
        return self.wait_for_visible(locator).is_displayed()