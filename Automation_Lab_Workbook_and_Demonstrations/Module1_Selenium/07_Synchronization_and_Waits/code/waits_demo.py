from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# SETUP

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # 1. IMPLICIT WAIT
    # ========================================================

    print("\n--- 1. Implicit Wait ---")

    driver.implicitly_wait(5)

    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    print("Implicit wait configured: PASS")

    # 2. EXPLICIT WAIT
    # ========================================================

    print("\n--- 2. Explicit Wait ---")

    input_box = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#input-example input")
        )
    )

    print("Input element located using explicit wait")
    print("Explicit wait: PASS")
    # 3. VISIBILITY OF ELEMENT
    print("\n--- 3. Visibility Check ---")
    wait.until(
        EC.visibility_of(input_box)
    )
    print("Input element is visible")
    print("Visibility wait: PASS")
    # ========================================================
    # 4. ELEMENT CLICKABLE
    # ========================================================

    print("\n--- 4. Element Clickable ---")

    enable_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#input-example button")
        )
    )

    print("Enable button is clickable")
    print("Clickable wait: PASS")


    # ========================================================
    # 5. CLICK AND WAIT FOR STATE CHANGE
    # ========================================================

    print("\n--- 5. Wait for Dynamic State Change ---")

    enable_button.click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#input-example input")
        )
    )

    print("Input became enabled")
    print("Dynamic state wait: PASS")


    # ========================================================
    # 6. TEXT VERIFICATION
    # ========================================================

    print("\n--- 6. Wait for Text ---")

    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    print("Message:", message.text)

    assert "It's enabled!" in message.text

    print("Expected text found")
    print("Text verification: PASS")


    # ========================================================
    # FINAL RESULT
    # ========================================================
    print("WAITS DEMO PASSED SUCCESSFULLY")



finally:

    driver.quit()