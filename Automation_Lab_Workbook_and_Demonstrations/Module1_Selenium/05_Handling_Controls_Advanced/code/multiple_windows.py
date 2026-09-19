# Objective:
# Open multiple browser windows/tabs and switch between them using Selenium.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create a Chrome browser session.
driver = webdriver.Chrome()
# Open the first website.
driver.get("https://example.com")

# Store the first window handle.
first_window = driver.current_window_handle

# Open a new tab.
driver.switch_to.new_window("tab")

# Open the second website in the new tab.
driver.get("https://www.selenium.dev")

# Store the second window handle.
second_window = driver.current_window_handle
print("Number of windows:", len(driver.window_handles))
print("Second window title:", driver.title)

# Switch back to the first window.
driver.switch_to.window(first_window)

print("First window title:", driver.title)
# Switch to the second window again.
driver.switch_to.window(second_window)

print("Switched back to second window:", driver.title)
time.sleep(7)  # Pause for 7 seconds to observe the actions.
# Close the current window and end the session.
driver.quit()