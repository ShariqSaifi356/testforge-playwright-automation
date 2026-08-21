from pages.base_page import BasePage

      
class HomePage(BasePage):
    
    HOME_PAGE_ELEMENT = "body"

    def home_page_element(self):
        return self.page.locator(self.HOME_PAGE_ELEMENT)   
    