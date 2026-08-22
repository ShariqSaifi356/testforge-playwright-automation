import pytest
from utils.browser_factory import BrowserFactory



# Command line cross browser set-up.
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        choices=["chromium", "firefox", "webkit"],
        help="Browser to run tests on"
    )

@pytest.fixture(scope="function")
def page(request):

    browser_name = request.config.getoption("--browser_name")
    factory = BrowserFactory()
    browser = factory.create_browser(browser_name)
    context = factory.create_context(browser)
    page = context.new_page()

    yield page

    factory.close(browser, context)