# Objective:
# Enter a date into a date input field using Selenium.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a Chrome browser session.
driver = webdriver.Chrome()

# Open Selenium practice form.
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Find the date input field.
date_picker = driver.find_element(By.NAME, "my-date")

# Enter the date.
date_picker.send_keys("09/08/2026")

print("Date entered successfully")

time.sleep(7)  # Pause for 7 seconds to observe the actions.
# Close browser.
driver.quit()