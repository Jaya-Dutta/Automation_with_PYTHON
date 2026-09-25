from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):

    signup_login = (By.CSS_SELECTOR, "a[href='/login']")
    products = (By.CSS_SELECTOR, "a[href='/products']")

    def open(self, url):
        self.open_url(url)

    def go_to_login(self):
        self.click(self.signup_login)

    def go_to_products(self):
        self.click(self.products)