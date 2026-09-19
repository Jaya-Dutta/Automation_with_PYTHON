from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("\n1. Open Web Page")
    driver.get("https://the-internet.herokuapp.com/login")
    print("Page opened successfully")
    print("\n2. Try Valid Element")
    try:
        username = driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        print("Username field found")
        print("Valid element handling: PASS")
    except NoSuchElementException:
        print("Username field not found")
    print("\n3. Handle Invalid Element")

    try:
        driver.find_element(By.ID, "invalid_element")

    except NoSuchElementException:
        print("Expected NoSuchElementException handled successfully")
        print("Exception handling: PASS")

    print("\n4. Finally Block")

finally:
    print("Finally block executed")
    driver.quit()
    print("Browser closed")

print("\nEXCEPTION HANDLING DEMO PASSED SUCCESSFULLY")