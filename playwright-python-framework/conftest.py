import sys
from pathlib import Path

import pytest
from utils.browser_factory import BrowserFactory
from utils.logger import get_logger


FRAMEWORK_DIR = Path(__file__).resolve().parent
SCREENSHOT_DIR = FRAMEWORK_DIR / "screenshots" / "traces"


# ---------------------------------------------------------
# Command line browser option
# ---------------------------------------------------------

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="append",
        default=None,
        choices=["chromium", "firefox", "webkit"],
        help="Browser to run tests on. Pass multiple times for cross-browser run, e.g. --browser_name=chromium --browser_name=firefox"
    )


def pytest_generate_tests(metafunc):
    if "page" in metafunc.fixturenames:
        browsers = metafunc.config.getoption("--browser_name") or ["chromium"]
        metafunc.parametrize("page", browsers, indirect=True, ids=browsers)
    
# For Screenshot 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    
# ---------------------------------------------------------
# Logger fixture
# ---------------------------------------------------------

@pytest.fixture(scope="function")
def logger(request):
    test_logger = get_logger(
        request.node.name
    )

    yield test_logger

    if request.node.rep_call.failed:
        test_logger.error(
            f"Test failed: {request.node.name}"
        )

@pytest.fixture(scope="function")
def page(request):

    browser_name = request.param
    factory = BrowserFactory()
    browser = factory.create_browser(browser_name)
    context = factory.create_context(browser)
    page = context.new_page()

    yield page
    
    # For Screenshot 
    if request.node.rep_call.failed:
        SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(SCREENSHOT_DIR / f"{request.node.name}.png"), full_page=True)
        
    factory.close(browser, context)