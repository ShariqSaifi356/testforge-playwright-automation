from playwright.sync_api import Page, Locator

class BasePage:
    
    def __init__(self, page:Page, logger):
        self.page = page
        self.logger = logger
        
    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url, wait_until="domcontentloaded")
        
    def click(self, locator:Locator):
        self.logger.info("Clicking element")
        locator.click()
            
    def fill(self, locator:Locator, value:str):
        self.logger.info("Entering value into field")
        locator.fill(value) 
        
    def inner_text(self, locator:Locator):
        self.logger.info("Getting element text")
        return locator.inner_text()  

    def check(self, locator:Locator):
        self.logger.info("Checking checkbox")
        locator.check()
        
    def select(self, locator:Locator, value):
        self.logger.info(f"Selecting option: {value}")
        locator.select_option(value)