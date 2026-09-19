# Objective:
# Demonstrate advanced CSS selectors in Selenium:
# basic CSS, starts-with, contains, ends-with, and child selector.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a Chrome browser session.
driver = webdriver.Chrome()

# Open Selenium's practice form.
driver.get("https://www.selenium.dev/selenium/web/web-form.html")


# 1. Basic CSS Selector
# # selects an element by its ID.
text_box = driver.find_element(By.CSS_SELECTOR, "#my-text-id")
text_box.send_keys("Jaya")

print("Basic CSS selector found:", text_box.get_attribute("id"))


# 2. CSS Starts-With Wildcard
# ^ means the attribute value starts with the given text.
starts_with = driver.find_element(
    By.CSS_SELECTOR, "[id^='my-']"
)

print("Starts-with selector found:", starts_with.get_attribute("id"))


# 3. CSS Contains Wildcard
# * means the attribute value contains the given text.
contains = driver.find_element(
    By.CSS_SELECTOR, "[id*='text']"
)

print("Contains selector found:", contains.get_attribute("id"))


# 4. CSS Ends-With Wildcard
# $ means the attribute value ends with the given text.
ends_with = driver.find_element(
    By.CSS_SELECTOR, "[id$='id']"
)

print("Ends-with selector found:", ends_with.get_attribute("id"))


# 5. CSS Child Selector
# > selects a direct child.
# <body> is a direct child of <html>.
child_element = driver.find_element(
    By.CSS_SELECTOR, "html > body"
)

print("Child selector found:", child_element.tag_name)

time.sleep(7)  # Pause for 2 seconds to observe the actions.
# Close the browser.
driver.quit()