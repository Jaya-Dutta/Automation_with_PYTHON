from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
driver = webdriver.Chrome()
driver.maximize_window()
screenshot_folder = Path(__file__).parent.parent / "screenshots"
screenshot_folder.mkdir(exist_ok=True)
def take_screenshot(driver, file_name):
    file_path = screenshot_folder / file_name
    driver.save_screenshot(str(file_path))
    print(f"Screenshot saved: {file_path}")
try:
    print("\n1. Open Web Page")
    driver.get("https://the-internet.herokuapp.com/login")
    print("Page opened successfully")
    print("\n2. Take Screenshot")
    take_screenshot(driver, "login_page.png")
    print("Screenshot capture: PASS")
    print("\n3. Perform Action")
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    take_screenshot(driver, "username_entered.png")
    print("Action screenshot: PASS")
    print("\n4. Final Validation")

    assert username.get_attribute("value") == "tomsmith"

    print("Screenshot method validation: PASS")
    print("\nSCREENSHOT DEMO PASSED SUCCESSFULLY")

finally:
    driver.quit()