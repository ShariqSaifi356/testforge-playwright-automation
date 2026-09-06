from pathlib import Path
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage


def test_case_6(page, logger):

    NAME = "Arpita"
    EMAIL = "arpita123456@gmail.com"
    SUBJECT = "TestForge contact form automation"
    MESSAGE = "This is an automated test of the contact form."
    FILE_PATH = Path(__file__).resolve().parent.parent / "data" / "contact_attachment.txt"

    home_page = HomePage(page, logger)
    contact_us_page = ContactUsPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_contact_us()

    logger.info("Verifying 'Get In Touch' heading")
    expect(contact_us_page.contact_heading).to_be_visible()
    expect(contact_us_page.contact_heading).to_have_text("Get In Touch")
    contact_us_page.enter_name(NAME)
    contact_us_page.enter_email(EMAIL)
    contact_us_page.enter_subject(SUBJECT)
    contact_us_page.enter_message(MESSAGE)
    contact_us_page.upload_attachment(FILE_PATH)
    contact_us_page.accept_next_dialog()
    contact_us_page.click_submit_button()

    logger.info("Verifying contact form success message")
    expect(contact_us_page.success_message).to_be_visible()
    expect(contact_us_page.success_message).to_have_text("Success! Your details have been submitted successfully.")
    contact_us_page.click_home_button()

    logger.info("Verifying user is navigated to home page")
    expect(page).to_have_url("https://automationexercise.com/")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
