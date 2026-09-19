# Objective:
# Open Firefox using Selenium WebDriver, visit a website,
# read the title and URL, then close the browser.

import time
from selenium import webdriver

# Create a Firefox WebDriver session.
driver = webdriver.Firefox()
# Open the website.
driver.get("https://example.com")

# Print basic browser information.
print("Browser: Firefox")
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(5)  # Wait for 5 seconds to see the page before closing.

# Close the browser and end the Selenium session.
driver.quit()