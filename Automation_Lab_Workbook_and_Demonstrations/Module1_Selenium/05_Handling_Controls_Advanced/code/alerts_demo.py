# Objective:
# Handle JavaScript alert, confirm, and prompt using Selenium.
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Create a Chrome browser session.
driver = webdriver.Chrome()
# Open Selenium's alert practice page.
driver.get("https://www.selenium.dev/selenium/web/alerts.html")
# 1. Handle Alert
# Click the button that opens an alert.
driver.find_element(By.ID, "alert").click()
# Switch to the alert popup.
alert = driver.switch_to.alert

# Print alert message.
print("Alert message:", alert.text)

# Accept the alert.
alert.accept()

print("Alert accepted")
# 2. Handle Confirm
# Click the button that opens a confirmation popup.
driver.find_element(By.ID, "confirm").click()

# Switch to the confirm popup.
confirm = driver.switch_to.alert

print("Confirm message:", confirm.text)
# Dismiss the confirm popup.
confirm.dismiss()
print("Confirm dismissed")
# 3. Handle Prompt
# Click the button that opens a prompt popup.
driver.find_element(By.ID, "prompt").click()
# Switch to the prompt popup.
prompt = driver.switch_to.alert

print("Prompt message:", prompt.text)
# Enter text into the prompt.
prompt.send_keys("Jaya")

# Submit the prompt.
prompt.accept()

print("Prompt submitted")
time.sleep(20)  # Pause for 20 seconds to observe the actions.
# Close browser.
driver.quit()