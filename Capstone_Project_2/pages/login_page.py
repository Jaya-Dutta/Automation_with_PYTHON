from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    email = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    password = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    login_button = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    logged_in_user = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    logout_link = (By.CSS_SELECTOR, "a[href='/logout']")

    def login(self, username, password):
        self.enter_text(self.email, username)
        self.enter_text(self.password, password)
        self.click(self.login_button)

    def is_logged_in(self):
        return self.wait_for_visible(self.logged_in_user).is_displayed()

    def logout(self):
        self.click(self.logout_link)