# Objective:
# Understand the basic WebDriver lifecycle:
# Create → Navigate → Read information → Quit.

import time
from selenium import webdriver

# 1. Create the browser session.
driver = webdriver.Chrome()

# 2. Navigate to a website.
driver.get("https://example.com")

# 3. Read browser/page information.
print("Window Handle:", driver.current_window_handle)
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# 4. End the WebDriver session.
driver.quit()

time.sleep(5)  # Wait for 5 seconds to ensure the browser has closed.
print("Browser session ended successfully.")