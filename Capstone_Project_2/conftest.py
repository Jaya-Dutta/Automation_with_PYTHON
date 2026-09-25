import pytest

from utilities.driver_factory import create_driver
from utilities.screenshot import save_screenshot
from utilities.logger import get_logger


logger = get_logger("TestFramework")


@pytest.fixture
def driver(request):
    logger.info("Starting test: %s", request.node.name)

    driver = create_driver()

    yield driver

    report = getattr(request.node, "rep_call", None)

    if report:
        status = "pass" if report.passed else "fail"

        logger.info(
            "Test completed: %s - %s",
            request.node.name,
            status.upper()
        )

        save_screenshot(driver, request.node.name, status)

    driver.quit()
    logger.info("Browser closed: %s", request.node.name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{report.when}", report)