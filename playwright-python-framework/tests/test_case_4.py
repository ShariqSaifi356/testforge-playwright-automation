from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_case_4(page, logger):
    
    EMAIL = "arpita123456@gmail.com"
    PASSWORD = "AaBb123@123SaaS"
    
    home_page = HomePage(page, logger)
    login_page = LoginPage(page, logger)
    
    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    
    home_page.click_singup_page()
    
    logger.info("Verifying 'Login to your account' heading")
    expect(login_page.login_heading).to_be_visible()
    expect(login_page.login_heading).to_have_text("Login to your account")
    
    login_page.enter_login_email(EMAIL)
    login_page.enter_login_password(PASSWORD)
    login_page.click_login_button()
    
    logger.info("Verifying 'Logged in as Arpita' text")
    expect(login_page.logged_in_username).to_be_visible()
    expect(login_page.username_visible).to_have_text("Arpita")
    
    logger.info("Clicking 'Logout' link")
    login_page.click_logout_button()
    
    logger.info("Verifying user is navigated to login page")
    expect(page).to_have_url("https://automationexercise.com/login")
    expect(login_page.login_heading).to_be_visible()
    expect(login_page.login_heading).to_have_text("Login to your account")
