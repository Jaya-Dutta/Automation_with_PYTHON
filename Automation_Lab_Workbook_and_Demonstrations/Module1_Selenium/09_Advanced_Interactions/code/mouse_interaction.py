from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path


driver = webdriver.Chrome()
driver.maximize_window()

screenshot_folder = Path(__file__).parent.parent / "screenshots"
screenshot_folder.mkdir(exist_ok=True)


def take_screenshot(name):
    driver.save_screenshot(str(screenshot_folder / name))
try:
    print("\n1. Double Click")

    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

    button = driver.find_element(By.XPATH, "//button[text()='Add Element']")

    ActionChains(driver).double_click(button).perform()

    take_screenshot("double_click.png")

    print("Double click: PASS")


    print("\n2. Right Click")

    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    box = driver.find_element(By.CSS_SELECTOR, ".context-menu-one")

    ActionChains(driver).context_click(box).perform()

    take_screenshot("right_click.png")

    print("Right click: PASS")


    print("\n3. Mouse Hover")

    driver.get("https://the-internet.herokuapp.com/hovers")

    users = driver.find_elements(By.CSS_SELECTOR, ".figure")

    ActionChains(driver).move_to_element(users[0]).perform()

    caption = users[0].find_element(By.CSS_SELECTOR, ".figcaption")

    assert caption.is_displayed()

    take_screenshot("mouse_hover.png")

    print("Mouse hover: PASS")


    print("\n4. Drag and Drop")

    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    source = driver.find_element(By.ID, "column-a")
    target = driver.find_element(By.ID, "column-b")

    ActionChains(driver).drag_and_drop(source, target).perform()

    take_screenshot("drag_and_drop.png")

    print("Drag and drop: PASS")


    print("\nADVANCED MOUSE ACTIONS DEMO PASSED SUCCESSFULLY")

finally:
    driver.quit()