from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.signup_page import SignupPage


def test_case_5(page, logger):

    NAME = "Arpita"
    EMAIL = "arpita123456@gmail.com"

    home_page = HomePage(page, logger)
    signup_page = SignupPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_singup_page()

    logger.info("Verifying 'New User Signup!' heading")
    expect(signup_page.signup_heading).to_be_visible()
    expect(signup_page.signup_heading).to_have_text("New User Signup!")
    signup_page.enter_name(NAME)
    signup_page.enter_signup_email(EMAIL)
    signup_page.click_signup_button()

    logger.info("Verifying 'Email Address already exist!' message")
    expect(signup_page.existing_email_message).to_be_visible()
    expect(signup_page.existing_email_message).to_have_text("Email Address already exist!")
