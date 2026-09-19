# Objective:
# Upload a file using Selenium's file input control.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path
# Create a Chrome browser session.
driver = webdriver.Chrome()

# Open Selenium's file upload practice page.
driver.get("https://the-internet.herokuapp.com/upload")

# Create the path of a sample file.
file_path = Path.cwd() / "sample.txt"

# Create the sample file.
file_path.write_text("This is a Selenium file upload test.")

# Find the file upload input.
upload_box = driver.find_element(By.ID, "file-upload")

# Select the file.
upload_box.send_keys(str(file_path))

# Click the Upload button.
driver.find_element(By.ID, "file-submit").click()

print("File uploaded successfully")
time.sleep(7)  # Pause for 7 seconds to observe the actions.
# Close the browser.
driver.quit()