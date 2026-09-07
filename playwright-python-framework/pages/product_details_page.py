import re
from pages.base_page import BasePage


class ProductDetailsPage(BasePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.product_details = page.locator(".product-information")
        self.product_name = self.product_details.get_by_role("heading", level=2)
        self.category = self.product_details.get_by_text(re.compile(r"^Category:\s*\S"))
        self.price = self.product_details.get_by_text(re.compile(r"^Rs\.\s*\d"))
        self.availability = self.product_details.locator("p").filter(has_text=re.compile(r"^Availability:\s*\S"))
        self.condition = self.product_details.locator("p").filter(has_text=re.compile(r"^Condition:\s*\S"))
        self.brand = self.product_details.locator("p").filter(has_text=re.compile(r"^Brand:\s*\S"))

    @property
    def quantity(self):
        return self.product_details.locator("input[name='quantity']")

    @property
    def add_to_cart_button(self):
        return self.product_details.get_by_role("button", name="Add to cart")

    def enter_quantity(self, quantity:str):
        self.fill(self.quantity, quantity)

    def click_add_to_cart(self):
        self.wait_for_page_load()
        self.click(self.add_to_cart_button)
