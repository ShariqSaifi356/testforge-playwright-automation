from playwright.sync_api import expect
from pages.home_page import HomePage

def test_home_page(page):
    
    home_page = HomePage(page)
    expect(home_page.home_page_element()).to_be_visible()
