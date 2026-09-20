import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Page Object: keeps page locators and actions together.
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.inventory = (By.CLASS_NAME, "inventory_list")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        return self.driver.find_element(*self.inventory).is_displayed()


# BDD-style scenario.
driver = webdriver.Chrome()
driver.maximize_window()

try:
    login_page = LoginPage(driver)

    # Given
    login_page.open()

    # When
    login_page.login("standard_user", "secret_sauce")

    # Then
    assert login_page.is_login_successful()

    print("Login successful - inventory page displayed.")

    # Save execution evidence.
    screenshot_dir = os.path.join(
        os.path.dirname(__file__),
        "screenshots"
    )
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(
        screenshot_dir,
        "assignment_3_pom_success.png"
    )

    driver.save_screenshot(screenshot_path)
    print("Screenshot saved:", screenshot_path)

    print("PASS: Assignment 3 - Selenium POM + BDD scenario completed.")

finally:
    time.sleep(2)
    driver.quit()