# Objective:
# Open Chrome using Selenium WebDriver, visit a website,
# read the title and URL, then close the browser.

import time
from selenium import webdriver

# Create a Chrome WebDriver session.
driver = webdriver.Chrome()

# Open the website.
driver.get("https://example.com")

# Print basic browser information.
print("Browser: Chrome")
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

time.sleep(15)  # Wait for 5 seconds to see the page before closing.
# Close the browser and end the Selenium session.
driver.quit()