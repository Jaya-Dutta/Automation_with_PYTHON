from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


# Create Chrome WebDriver
driver = webdriver.Chrome()

# Screenshot folder
screenshot_dir = Path(__file__).resolve().parent.parent / "screenshots"
screenshot_dir.mkdir(exist_ok=True)

try:
    # Open JavaScript alerts practice page
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    # ---------------------------------------------------------
    # 1. JavaScript Alert → Accept
    # ---------------------------------------------------------

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Alert']"
    ).click()

    alert = driver.switch_to.alert
    alert.accept()

    assert driver.find_element(By.ID, "result").text == "You successfully clicked an alert"

    print("JavaScript Alert accepted successfully!")


    # ---------------------------------------------------------
    # 2. JavaScript Confirm → Dismiss
    # ---------------------------------------------------------

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Confirm']"
    ).click()

    confirm = driver.switch_to.alert
    confirm.dismiss()

    assert driver.find_element(By.ID, "result").text == "You clicked: Cancel"

    print("JavaScript Confirm dismissed successfully!")


    # ---------------------------------------------------------
    # 3. JavaScript Prompt → Enter text and Accept
    # ---------------------------------------------------------

    driver.find_element(
        By.XPATH, "//button[text()='Click for JS Prompt']"
    ).click()

    prompt = driver.switch_to.alert

    # Enter text directly into the JavaScript prompt
    prompt.send_keys("Jaya")

    # Submit the prompt
    prompt.accept()

    result = driver.find_element(By.ID, "result").text

    assert result == "You entered: Jaya"

    print("JavaScript Prompt handled successfully!")
    print("Prompt result:", result)


    # ---------------------------------------------------------
    # 4. Automatic screenshot
    # ---------------------------------------------------------

    screenshot_path = screenshot_dir / "assignment4_success.png"
    driver.save_screenshot(str(screenshot_path))

    print("Screenshot saved:", screenshot_path)


finally:
    # Close browser
    driver.quit()