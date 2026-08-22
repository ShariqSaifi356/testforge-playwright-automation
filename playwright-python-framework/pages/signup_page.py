from pages.base_page import BasePage

class SignupPage(BasePage):
    
    def __init__(self, page):
         super().__init__(page)
         
         self.signup_heading = page.get_by_role("heading", name="New User Signup!", exact=True)
         self.name = page.get_by_role("textbox", name="Name")
         self.email = page.get_by_role("textbox", name="Email Address").nth(1)
         self.signup_button = page.get_by_role("button", name="Signup", exact=True)
         self.signup_heading_2 = page.locator("//b[normalize-space()='Enter Account Information']")
         self.title = page.get_by_role("radio", name="Mr.")
         self.password = page.locator("#password")
         self.day = page.locator("//select[@id='days']")
         self.month = page.locator("#months")
         self.year = page.locator("#years")
         self.newsletter = page.get_by_role("checkbox", name="Sign up for our newsletter!")
         self.specialoffers = page.get_by_role("checkbox", name="Receive special offers from our partners!")
         self.signup_heading_3 = page.locator("//b[normalize-space()='Address Information']")
         self.firt_name = page.get_by_role("textbox", name="First name *")
         self.last_name = page.get_by_role("textbox", name="Last name *")
         self.company = page.get_by_label("Company", exact=True)
         self.address = page.locator("//input[@id='address1']")
         self.address_2 = page.locator("//input[@id='address2']")
         self.country = page.get_by_role("combobox", name="Country *")
         self.state = page.get_by_role("textbox", name="State *")
         self.zipcode = page.locator("//input[@id='zipcode']")
         self.mobile_number = page.get_by_role("textbox", name="Mobile Number *")
         self.create_account_button = page.get_by_role("button", name="Create Account")
         self.signup_heading_4 = page.locator("//b[normalize-space()='Account Created!']")
         self.continue_button = page.get_by_role("link", name="Continue")
         self.username_visible = page.get_by_text("Rohan", exact=True)
         self.delete_button = page.get_by_role("link", name="Delete Account")
         self.signup_heading_5 = page.locator("//b[normalize-space()='Account Deleted!']")
    
    def enter_name(self, name:str):
        self.fill(self.name, name)
        
    def enter_email(self, email:str):
        self.fill(self.email, email)
    
    def click_signup_button(self):
        self.click(self.signup_button)
        
    def select_title(self):
        self.check(self.title)
        
    def enter_password(self, password:str):
        self.fill(self.password, password)
        
    def select_day(self, value):
        self.select(self.day, value)
        
    def select_month(self, value):
        self.select(self.month, value)
        
    def select_year(self, value):
        self.select(self.year, value)
    
    def select_newsletter(self):
        self.check(self.newsletter)
        
    def select_specialoffers(self):
        self.check(self.specialoffers)
        
    def enter_first_name(self, firstName):
        self.fill(self.firt_name, firstName)
        
    def enter_last_name(self, lastName):
        self.fill(self.last_name, lastName)
        
    def enter_company(self, company):
        self.fill(self.company, company)
        
    def enter_address(self, address):
        self.fill(self.address, address)
        
    def enter_address_2(self, address):
        self.fill(self.address, address)
        
    def select_country(self, value):
        self.select(self.country, value)
        
    def select_state(self, state):
        self.fill(self.state, state)
        
    def enter_zip_code(self, zipCode):
        self.fill(self.zipcode, zipCode)
        
    def enter_mobile_number(self, mobileNumber):
        self.fill(self.mobile_number, mobileNumber)
    
    def click_create_account(self):
        self.click(self.create_account_button)
        
    def click_continue(self):
        self.click(self.continue_button)
        
    def click_delete(self):
        self.click(self.delete_button)