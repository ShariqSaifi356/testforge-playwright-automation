from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage


def test_case_7(page, logger):

    home_page = HomePage(page, logger)
    test_cases_page = TestCasesPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_test_cases()

    logger.info("Verifying user is navigated to test cases page")
    expect(page).to_have_url("https://automationexercise.com/test_cases")
    expect(test_cases_page.test_cases_heading).to_be_visible()
    expect(test_cases_page.test_cases_heading).to_have_text("Test Cases")
