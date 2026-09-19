from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
try:
    print("\n1. Dynamic Loading")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    start_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()
    print("Loading started")
    # Wait until the dynamically loaded element becomes visible
    result = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    print("Loaded text:", result.text)
    assert result.text == "Hello World!"
    print("Dynamic loading: PASS")
    print("\n2. Presence of Element")
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#start button"))
    )
    print("Start button is present")
    print("Presence check: PASS")

    print("\n3. Visibility of Element")
    wait.until(
        EC.visibility_of(start_button)
    )
    print("Start button is visible")
    print("Visibility check: PASS")
    print("\n4. Element Clickable")

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    ).click()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    assert "Hello World!" in result.text

    print("Element became clickable and loaded successfully")
    print("Clickable wait: PASS")


    print("\n5. Final Validation")

    assert result.is_displayed()
    assert result.text == "Hello World!"

    print("Dynamic content validated")
    print("Final validation: PASS")

    print("\nWAITS DEMO PASSED SUCCESSFULLY")

finally:
    driver.quit()