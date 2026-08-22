from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_case_1(page):
    
    NAME = "Arpita"
    EMAIL = f"arpita{__import__('uuid').uuid4().hex[:6]}@gmail.com"
    PASSWORD = "AaBb123@123SaaS"
    DAY = "6"
    MONTH = "11"
    YEAR = "1998"
    FIRST_NAME = "Arpit"
    LAST_NAME = "Singh"
    COMPANY = "ImpactQA"
    ADDRESS = "69A, Sector 10A, Gurgaon"
    ADDRESS_2 = "India"
    COUNTRY = "India"
    STATE = "HR"
    CITY = "Gurgaon"
    ZIPCODE = "120001"
    MOBILE_NUMBER = "9000000001"
    
    home_page = HomePage(page)  
    signup_page = SignupPage(page) 
    
    home_page.navigate("https://automationexercise.com/")
    
    expect(home_page.home_page_element).to_be_visible()
    home_page.click_singup_page()
    
    expect(signup_page.signup_heading).to_have_text("New User Signup!")
    signup_page.enter_name(NAME)
    signup_page.enter_email(EMAIL)
    signup_page.click_signup_button()
    
    expect(signup_page.signup_heading_2).to_have_text("Enter Account Information")    
    signup_page.select_title()
    signup_page.enter_password(PASSWORD)
    signup_page.select_day(DAY)
    signup_page.select_month(MONTH)
    signup_page.select_year(YEAR)
    signup_page.select_newsletter()
    signup_page.select_specialoffers()
    expect(signup_page.signup_heading_3).to_have_text("Address Information")
    signup_page.enter_first_name(FIRST_NAME)
    signup_page.enter_last_name(LAST_NAME)
    signup_page.enter_company(COMPANY)
    signup_page.enter_address(ADDRESS)
    signup_page.enter_address_2(ADDRESS_2)
    signup_page.select_country(COUNTRY)
    signup_page.select_state(STATE)
    signup_page.enter_city(CITY)
    signup_page.enter_zip_code(ZIPCODE)
    signup_page.enter_mobile_number(MOBILE_NUMBER)
    signup_page.click_create_account()
    expect(signup_page.signup_heading_4).to_have_text("Account Created!")
    signup_page.click_continue()
    expect(signup_page.username_visible).to_have_text("Arpita")
    signup_page.click_delete()
    expect(signup_page.signup_heading_5).to_have_text("Account Deleted!")
    signup_page.click_continue()