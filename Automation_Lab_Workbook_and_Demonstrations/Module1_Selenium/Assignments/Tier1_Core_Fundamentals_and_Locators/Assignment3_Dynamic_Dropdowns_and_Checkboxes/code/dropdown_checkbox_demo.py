from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By


# Create Chrome WebDriver
driver = webdriver.Chrome()

# Screenshot folder
screenshot_dir = Path(__file__).resolve().parent.parent / "screenshots"
screenshot_dir.mkdir(exist_ok=True)

try:
    # Open Selenium official practice form
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # ---------------------------------------------------------
    # 1. Handle checkboxes
    # ---------------------------------------------------------

    checkboxes = driver.find_elements(
        By.CSS_SELECTOR, "input[type='checkbox']"
    )

    # Select the first two checkboxes
    for checkbox in checkboxes[:2]:
        if not checkbox.is_selected():
            checkbox.click()

        assert checkbox.is_selected()

    print("Checkboxes selected successfully!")


    # ---------------------------------------------------------
    # 2. Handle searchable datalist
    # ---------------------------------------------------------

    # Locate the datalist input using its list attribute
    search_box = driver.find_element(
        By.CSS_SELECTOR, "input[list='my-options']"
    )

    # Find all available suggestions
    suggestions = driver.find_elements(
        By.CSS_SELECTOR, "#my-options option"
    )

    target = "New York"

    # Loop through suggestions and find the matching option
    for option in suggestions:
        if option.get_attribute("value") == target:
            search_box.send_keys(target)
            break
    else:
        raise AssertionError(f"Suggestion '{target}' was not found.")

    # Verify entered value
    assert search_box.get_attribute("value") == target

    print("Matching dropdown option selected:", target)


    # ---------------------------------------------------------
    # 3. Automatic screenshot
    # ---------------------------------------------------------

    screenshot_path = screenshot_dir / "assignment3_success.png"

    driver.save_screenshot(str(screenshot_path))

    print("Screenshot saved:", screenshot_path)


finally:
    # Close browser
    driver.quit()