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

    def upload_file(self, locator:Locator, file_path):
        self.logger.info("Uploading file")
        locator.set_input_files(file_path)

    def scroll_to(self, locator:Locator):
        self.logger.info("Scrolling to element")
        locator.scroll_into_view_if_needed()

    def accept_next_dialog(self):
        self.logger.info("Accepting next browser dialog")
        self.page.once("dialog", lambda dialog: dialog.accept())

    def wait_for_page_load(self):
        self.logger.info("Waiting for page scripts and resources to load")
        self.page.wait_for_load_state("load")

    def hover(self, locator:Locator):
        self.logger.info("Hovering over element")
        locator.hover()
