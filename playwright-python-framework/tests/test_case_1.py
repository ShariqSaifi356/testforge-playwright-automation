from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_case_1(page):
    
    home_page = HomePage(page)  
    signup_page = SignupPage(page) 
    
    expect(home_page.home_page()).to_be_visible
    home_page.home_page_signup_login()
    # expect(signup_page.signup_page_heading()).to_have_text("New User Signup!")
    assert signup_page.signup_page_heading() == "New User Signup!"
    
