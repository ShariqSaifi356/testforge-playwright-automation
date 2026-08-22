
class BasePage:
    
    def __init__(self, page):
        self.page = page
        
    def click(self, role, name=None, exact=False):
        self.page.get_by_role(role, name=name, exact=exact).click()
        
    def inner_text(self, role, name=None, exact=False):
        return self.page.get_by_role(role, name=name, exact=exact).inner_text()
        
        