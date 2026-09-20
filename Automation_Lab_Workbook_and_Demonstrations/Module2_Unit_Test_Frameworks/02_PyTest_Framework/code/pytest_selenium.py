import pytest
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By

# Save screenshots inside the module's screenshots folder
SCREENSHOT_DIR = Path(__file__).parent.parent / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)

@pytest.fixture
def driver():
    """Create browser before test and close it after test."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.quit()

def test_google_search_page(driver):
    """Test Google page loading and search box."""
    driver.get("https://www.google.com")

    # Verify the page title
    assert "Google" in driver.title

    # Find the Google search box
    search_box = driver.find_element(By.NAME, "q")

    # Verify the search box is visible and enabled
    assert search_box.is_displayed()
    assert search_box.is_enabled()

    # Take browser screenshot as test evidence
    screenshot_path = SCREENSHOT_DIR / "google_test_passed.png"
    driver.save_screenshot(str(screenshot_path))