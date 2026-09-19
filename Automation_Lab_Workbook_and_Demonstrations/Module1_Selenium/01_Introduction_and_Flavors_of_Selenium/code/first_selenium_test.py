# Objective:
# Open a browser, visit a website, read its title, and close the browser.

import time
from selenium import webdriver

# Create a Chrome browser session.
driver = webdriver.Chrome()

# Open the website.
driver.get("https://example.com")

# Print the page title.
print("Page Title:", driver.title)
time.sleep(5)  # Wait for 5 seconds to see the page before closing.
# Close the browser and end the Selenium session.
driver.quit()