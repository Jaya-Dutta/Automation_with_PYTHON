from selenium import webdriver
from selenium.webdriver.common.by import By


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:
    # ---------------------------------------------------------
    # 1. Handle multiple windows / tabs
    # ---------------------------------------------------------

    driver.get("https://the-internet.herokuapp.com/windows")

    # Store the original window
    main_window = driver.current_window_handle

    # Open a new window
    driver.find_element(By.LINK_TEXT, "Click Here").click()

    # Get all open windows
    windows = driver.window_handles

    # Switch to the newly opened window
    for window in windows:
        if window != main_window:
            driver.switch_to.window(window)
            break

    # Validate new window
    assert driver.title == "New Window"

    print("New window opened successfully!")
    print("New window title:", driver.title)

    # Close new window
    driver.close()

    # Return to main window
    driver.switch_to.window(main_window)

    print("Returned to main window successfully!")


    # ---------------------------------------------------------
    # 2. Handle IFrame
    # ---------------------------------------------------------

    driver.get("https://the-internet.herokuapp.com/iframe")

    # Switch into the iframe
    iframe = driver.find_element(By.ID, "mce_0_ifr")
    driver.switch_to.frame(iframe)

    # Locate the editor body
    editor = driver.find_element(By.ID, "tinymce")

    # Select existing content and replace it
    editor.click()
    editor.send_keys("Selenium IFrame Test")

    # Read the text using textContent
    iframe_text = editor.get_attribute("textContent")

    # Validate iframe text
    assert "Selenium IFrame Test" in iframe_text

    print("IFrame handled successfully!")
    print("Text inside IFrame:", iframe_text)

    # Switch back to the main page
    driver.switch_to.default_content()

    print("Returned to main page successfully!")


finally:
    # Close browser
    driver.quit()