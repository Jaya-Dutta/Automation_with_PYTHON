from datetime import datetime
from pathlib import Path

import pytest


SCREENSHOT_DIR = Path(__file__).parent / "screenshots"
SCREENSHOT_DIR.mkdir(exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically take a screenshot when a test fails.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_path = SCREENSHOT_DIR / f"{test_name}_{timestamp}.png"

            driver.save_screenshot(str(screenshot_path))

            print(f"\nFailure screenshot saved: {screenshot_path}")