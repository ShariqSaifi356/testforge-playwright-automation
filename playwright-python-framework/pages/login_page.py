from pages.base_page import BasePage

class LoginPage(BasePage):
    
    def __init__(self, page, logger):
        super().__init__(page, logger)
        
        self.login_heading = page.get_by_role("heading", name="Login to your account", exact=True)
        self.email = page.get_by_role("textbox", name="Email Address").nth(0)
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.username_visible = page.get_by_text("Arpita", exact=True)
        self.worng_email_password_message = page.get_by_text("Your email or password is incorrect!")
        
    def enter_login_email(self, email:str):
        self.fill(self.email, email)
        
    def enter_login_password(self, password:str):
        self.fill(self.password, password)   
        
    def click_login_button(self):
        self.click(self.login_button)         