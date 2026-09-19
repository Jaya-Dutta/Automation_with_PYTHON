from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path

driver = webdriver.Chrome()
driver.maximize_window()
screenshot_folder = Path(__file__).parent.parent / "screenshots"
screenshot_folder.mkdir(exist_ok=True)

def take_screenshot(name):
    driver.save_screenshot(str(screenshot_folder / name))

try:
    print("\n1. Keyboard Actions")
    driver.get("https://the-internet.herokuapp.com/login")
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")
    username.send_keys(Keys.TAB)
    take_screenshot("keyboard_input.png")
    assert driver.find_element(By.ID, "password").is_displayed()
    print("Keyboard input and TAB: PASS")

    print("\n2. Keyboard Shortcut")
    username = driver.find_element(By.ID, "username")
    username.send_keys(Keys.CONTROL, "a")
    username.send_keys("tomsmith")
    take_screenshot("keyboard_shortcut.png")
    assert username.get_attribute("value") == "tomsmith"
    print("Keyboard shortcut: PASS")

    print("\n3. Scroll Down")
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")
    ActionChains(driver).scroll_by_amount(0, 800).perform()
    take_screenshot("scroll_down.png")
    print("Scroll down: PASS")

    print("\n4. Scroll to Element")
    driver.get("https://the-internet.herokuapp.com/large")
    target = driver.find_element(By.ID, "page-footer")
    ActionChains(driver).scroll_to_element(target).perform()
    take_screenshot("scroll_to_element.png")
    print("Scroll to element: PASS")

    print("\nADVANCED KEYBOARD AND SCROLL DEMO PASSED SUCCESSFULLY")
finally:
    driver.quit()