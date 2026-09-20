from datetime import datetime
from pathlib import Path

import pytest
import pytest_html
from selenium import webdriver


# Assignment 9 root folder
PROJECT_ROOT = Path(__file__).parent

# Store failure screenshots here
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.fixture
def driver():
    """
    Start Chrome before each test
    and close it after the test.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot when a test fails
    and embed it into the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            # Create a unique screenshot filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = SCREENSHOT_DIR / screenshot_name

            # Save screenshot as a PNG file
            driver.save_screenshot(str(screenshot_path))

            # Get screenshot as base64 text for pytest-html
            screenshot_base64 = driver.get_screenshot_as_base64()

            # Embed screenshot inside HTML report
            report.extras = getattr(report, "extras", [])
            report.extras.append(
                pytest_html.extras.png(screenshot_base64)
            )

            print(
                f"\nFailure screenshot saved: {screenshot_path}"
            )