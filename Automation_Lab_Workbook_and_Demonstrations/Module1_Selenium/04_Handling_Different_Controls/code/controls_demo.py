# Objective:
# Demonstrate XPath and common web controls:
# input box, button, checkbox, radio button, and select box.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# Create a Chrome browser session.
driver = webdriver.Chrome()
# Open Selenium's practice form.
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
# 1. Input Box using Relative XPath
# Find the text box using its ID through XPath.
text_box = driver.find_element(By.XPATH, "//input[@id='my-text-id']")
text_box.clear()
text_box.send_keys("Jaya")

# 2. Password Input using XPath
password = driver.find_element(By.XPATH, "//input[@name='my-password']")
password.send_keys("12345")

# 3. Button using XPath
# Find the Submit button by its text.
button = driver.find_element(By.XPATH, "//button[text()='Submit']")
print("Button found:", button.text)
# 4. Checkbox
# Select the first checkbox if it is not already selected.
checkbox = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")[0]

if not checkbox.is_selected():
    checkbox.click()

print("Checkbox selected:", checkbox.is_selected())

# 5. Radio Button
# Select the first radio button.
radio = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")[0]

if not radio.is_selected():
    radio.click()
print("Radio selected:", radio.is_selected())
# 6. Select Box / Dropdown
# Find the dropdown and select an option by visible text.
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_visible_text("Two")
print("Selected option:", dropdown.first_selected_option.text)
time.sleep(20)  # Pause for 2 seconds to observe the actions.
# Close the browser.
driver.quit()