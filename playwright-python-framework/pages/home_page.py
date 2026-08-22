from playwright.sync_api import Page
from pages.base_page import BasePage

      
class HomePage(BasePage):
    
    def __init__(self, page:Page):
        super().__init__(page)
        
        self.home_page_element = page.locator("body")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
      
    def click_singup_page(self):
        self.click(self.signup_login_link)