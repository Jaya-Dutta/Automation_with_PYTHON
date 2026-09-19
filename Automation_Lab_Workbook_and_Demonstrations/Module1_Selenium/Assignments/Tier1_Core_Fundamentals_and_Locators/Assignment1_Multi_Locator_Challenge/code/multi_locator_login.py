from selenium import webdriver
from selenium.webdriver.common.by import By


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open SauceDemo login page
    driver.get("https://www.saucedemo.com/")

    # Username → By.ID
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    # Password → By.NAME
    password = driver.find_element(By.NAME, "password")
    password.send_keys("secret_sauce")

    # Login button → By.XPATH
    login_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    login_button.click()

    # Validate successful login using the resulting URL
    assert "/inventory.html" in driver.current_url

    print("Login successful!")
    print("Current URL:", driver.current_url)

finally:
    # Close the browser
    driver.quit()