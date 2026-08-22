from pages.base_page import BasePage

class SignupPage(BasePage):
    
    SIGNUP_HEADING_TEXT = ("heading", "New User Signup!")
    
    
    def signup_page_heading(self):
        role, name = self.SIGNUP_HEADING_TEXT  
        return self.inner_text(role=role, name=name)