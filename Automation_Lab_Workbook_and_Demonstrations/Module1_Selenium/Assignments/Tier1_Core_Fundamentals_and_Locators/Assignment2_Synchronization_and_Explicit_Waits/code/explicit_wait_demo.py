from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open a page with dynamic content
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    # Click Start
    driver.find_element(By.CSS_SELECTOR, "#start button").click()

    # Explicit wait until the dynamic text becomes visible
    wait = WebDriverWait(driver, 10)
    message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # Extract and validate the dynamic text
    text = message.text

    assert text == "Hello World!"

    print("Dynamic content loaded successfully!")
    print("Extracted text:", text)

finally:
    # Close the browser
    driver.quit()