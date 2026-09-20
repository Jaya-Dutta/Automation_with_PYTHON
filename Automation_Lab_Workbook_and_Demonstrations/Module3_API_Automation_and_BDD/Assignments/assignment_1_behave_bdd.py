import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Given: Start the browser and open the application.
def given_application_is_open():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    return driver


# When: Enter valid login details and submit.
def when_user_logs_in(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


# Then: Verify successful login and capture evidence.
def then_login_should_be_successful(driver):
    inventory = driver.find_element(By.CLASS_NAME, "inventory_list")
    assert inventory.is_displayed()

    print("Login successful - inventory page displayed.")

    # Save screenshot after successful login.
    screenshot_dir = os.path.join(
        os.path.dirname(__file__),
        "screenshots"
    )
    os.makedirs(screenshot_dir, exist_ok=True)

    screenshot_path = os.path.join(
        screenshot_dir,
        "assignment_1_login_success.png"
    )

    driver.save_screenshot(screenshot_path)
    print("Screenshot saved:", screenshot_path)


# Execute the BDD-style end-to-end scenario.
driver = given_application_is_open()

try:
    when_user_logs_in(driver)
    then_login_should_be_successful(driver)
    print("PASS: Assignment 1 - Selenium + BDD scenario completed.")
finally:
    time.sleep(2)
    driver.quit()