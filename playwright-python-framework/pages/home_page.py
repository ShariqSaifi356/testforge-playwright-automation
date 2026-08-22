from pages.base_page import BasePage

      
class HomePage(BasePage):
    
    HOME_PAGE_ELEMENT = "body"
    SIGNUP_LOGIN_LINK = ("link", "Signup / Login")

    def home_page(self):
        return self.page.locator(self.HOME_PAGE_ELEMENT)
    
    def home_page_signup_login(self):
        role, name = self.SIGNUP_LOGIN_LINK
        return self.click(role=role, name=name)       
    