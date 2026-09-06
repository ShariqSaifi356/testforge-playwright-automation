from playwright.sync_api import expect
from pages.home_page import HomePage


def test_case_10(page, logger):

    EMAIL = f"arpita{__import__('uuid').uuid4().hex[:6]}@example.com"

    home_page = HomePage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.scroll_to_footer()

    logger.info("Verifying 'Subscription' heading")
    expect(home_page.subscription_heading).to_be_visible()
    expect(home_page.subscription_heading).to_have_text("Subscription")
    home_page.enter_subscription_email(EMAIL)
    home_page.click_subscribe()

    logger.info("Verifying subscription success message")
    expect(home_page.subscription_success_message).to_be_visible()
    expect(home_page.subscription_success_message).to_have_text("You have been successfully subscribed!")
