from playwright.sync_api import Page
from pages.base_page import BasePage

      
class HomePage(BasePage):
    
    def __init__(self, page:Page, logger):
        super().__init__(page, logger)
        
        self.home_page_element = page.locator("body")
        self.signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.header = page.get_by_role("banner")
        self.contact_us_link = self.header.get_by_role("link", name="Contact us")
        self.test_cases_link = self.header.get_by_role("link", name="Test Cases")
        self.products_link = self.header.get_by_role("link", name="Products")
        self.features_heading = page.get_by_role("heading", name="Features Items", exact=True)
        self.footer = page.get_by_role("contentinfo")
        self.subscription_heading = self.footer.get_by_role("heading", name="Subscription", exact=True)
        self.subscription_email = self.footer.get_by_placeholder("Your email address", exact=True)
        self.subscribe_button = self.footer.locator("button[type='submit']")
        self.subscription_success_message = self.footer.get_by_text("You have been successfully subscribed!", exact=True)
      
    def click_singup_page(self):
        self.click(self.signup_login_link)

    def click_contact_us(self):
        self.click(self.contact_us_link)

    def click_test_cases(self):
        self.click(self.test_cases_link)

    def click_products(self):
        self.click(self.products_link)

    def scroll_to_footer(self):
        self.scroll_to(self.footer)

    def enter_subscription_email(self, email:str):
        self.fill(self.subscription_email, email)

    def click_subscribe(self):
        self.wait_for_page_load()
        self.click(self.subscribe_button)
