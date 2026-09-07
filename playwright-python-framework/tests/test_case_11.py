from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_case_11(page, logger):

    EMAIL = f"arpita{__import__('uuid').uuid4().hex[:8]}@example.com"

    home_page = HomePage(page, logger)
    cart_page = CartPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_cart()

    logger.info("Verifying cart page and subscription heading")
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    expect(cart_page.cart_heading).to_be_visible()
    cart_page.scroll_to(cart_page.footer)
    expect(cart_page.subscription_heading).to_be_visible()
    expect(cart_page.subscription_heading).to_have_text("Subscription")
    cart_page.fill(cart_page.subscription_email, EMAIL)
    cart_page.wait_for_page_load()
    cart_page.click(cart_page.subscribe_button)

    logger.info("Verifying subscription success message")
    expect(cart_page.subscription_success_message).to_be_visible()
    expect(cart_page.subscription_success_message).to_have_text("You have been successfully subscribed!")
