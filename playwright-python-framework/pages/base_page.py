from playwright.sync_api import Page, Locator

class BasePage:
    
    def __init__(self, page:Page):
        self.page = page
        
    def click(self, locator:Locator):
        locator.click()
            
    def fill(self, locator:Locator, value:str):
        locator.fill(value) 
        
    def inner_text(self, locator:Locator):
        return locator.inner_text()  

    def check(self, locator:Locator):
        locator.check()
        
    def select(self, locator:Locator, value):
        locator.select_option(value)