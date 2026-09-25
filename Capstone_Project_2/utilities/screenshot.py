from pathlib import Path


screenshot_dir = Path(__file__).resolve().parent.parent / "screenshots"


def save_screenshot(driver, test_name, status):
    screenshot_dir.mkdir(exist_ok=True)

    file_name = f"{test_name}_{status}.png"
    file_path = screenshot_dir / file_name

    driver.save_screenshot(str(file_path))
    