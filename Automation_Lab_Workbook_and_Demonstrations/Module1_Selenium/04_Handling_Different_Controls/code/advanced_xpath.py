# Objective:
# Demonstrate advanced XPath:
# contains, starts-with, parent node, and sibling node.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create Chrome browser.
driver = webdriver.Chrome()

# Open Selenium practice form.
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# 1. XPath Contains
contains_element = driver.find_element(
    By.XPATH, "//input[contains(@id, 'text')]"
)
print("Contains XPath found:", contains_element.get_attribute("id"))

# 2. XPath Starts-With
starts_element = driver.find_element(
    By.XPATH, "//input[starts-with(@id, 'my-')]"
)
print("Starts-with XPath found:", starts_element.get_attribute("id"))

# 3. XPath Parent Node
text_box = driver.find_element(By.ID, "my-text-id")

parent = text_box.find_element(By.XPATH, "..")

print("Parent tag:", parent.tag_name)

# 4. XPath Sibling Node
# Find an input that is a sibling of another input
# inside the same parent container.
sibling = driver.find_element(
    By.XPATH, "//input[@id='my-text-id']/following::input[1]"
)

print("Sibling input found:", sibling.get_attribute("type"))
time.sleep(20)  # Pause for 20 seconds to observe the actions.
# Close browser.
driver.quit()