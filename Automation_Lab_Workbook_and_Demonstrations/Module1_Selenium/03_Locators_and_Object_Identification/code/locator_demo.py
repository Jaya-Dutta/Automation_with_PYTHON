# Objective:
# Demonstrate common Selenium locators on a single web page.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a Chrome browser session.
driver = webdriver.Chrome()

# Open Selenium's practice form.
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. ID Locator
# Find the text box using its ID.
text_box = driver.find_element(By.ID, "my-text-id")
text_box.send_keys("Jaya")

# 2. Name Locator
# Find the password field using its name attribute.
password_box = driver.find_element(By.NAME, "my-password")
password_box.send_keys("12345")

# 3. Tag Name Locator
# Find all input elements on the page.
input_elements = driver.find_elements(By.TAG_NAME, "input")
print("Number of input elements:", len(input_elements))

# 4. Link Text Locator
# Find the link using its complete visible text.
link = driver.find_element(By.LINK_TEXT, "Return to index")
print("Link text:", link.text)

# 5. Class Name Locator
# Find the element using its CSS class.
text_element = driver.find_element(By.CLASS_NAME, "display-6")
print("Class element text:", text_element.text)

# 6. CSS Selector
# Find the text box using a CSS selector.
css_text_box = driver.find_element(By.CSS_SELECTOR, "#my-text-id")
print("CSS locator found:", css_text_box.get_attribute("id"))

# 7. CSS Child Selector
# Find the first input element inside the form.
child_input = driver.find_element(By.CSS_SELECTOR, "form input")
print("Child input found:", child_input.get_attribute("type"))

time.sleep(7)  # Pause for 2 seconds to observe the actions.
# Close the browser.
driver.quit()