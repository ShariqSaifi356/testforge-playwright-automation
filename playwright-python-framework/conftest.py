import pytest
from utils.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def page():

    factory = BrowserFactory()

    browser = factory.create_browser()

    context = factory.create_context(browser)

    page = context.new_page()

    yield page

    factory.close(browser, context)