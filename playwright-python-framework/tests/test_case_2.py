import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage

# @pytest.mark.skip(reason="Just testing skip marker")
def test_case_2(page, logger):
    
    EMAIL = "arpita123456@gmail.com"
    PASSWORD = "AaBb123@123SaaS"
    
    home_page = HomePage(page, logger)  
    login_page = LoginPage(page, logger)
        
    home_page.navigate("https://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    
    home_page.click_singup_page()
    
    logger.info("Verifying 'Login to your account' heading")
    expect(login_page.login_heading).to_have_text("Login to your account")
    
    login_page.enter_login_email(EMAIL)
    login_page.enter_login_password(PASSWORD)
    login_page.click_login_button()
    
    logger.info("Verifying 'Arpita' text")
    expect(login_page.username_visible).to_have_text("Arpita")
    