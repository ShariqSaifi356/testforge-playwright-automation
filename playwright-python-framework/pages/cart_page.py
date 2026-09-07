from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.cart_heading = page.get_by_text("Shopping Cart", exact=True)
        self.cart_table = page.locator("#cart_info")
        self.product_rows = self.cart_table.get_by_role("row").filter(has=page.locator(".cart_description"))
        self.proceed_to_checkout = page.get_by_text("Proceed To Checkout", exact=True)
        self.register_login_link = page.get_by_role("link", name="Register / Login", exact=True)
        self.footer = page.get_by_role("contentinfo")
        self.subscription_heading = self.footer.get_by_role("heading", name="Subscription", exact=True)
        self.subscription_email = self.footer.get_by_placeholder("Your email address", exact=True)
        self.subscribe_button = self.footer.locator("button[type='submit']")
        self.subscription_success_message = self.footer.get_by_text("You have been successfully subscribed!", exact=True)

    def product_row(self, product_name:str):
        return self.product_rows.filter(has=self.page.get_by_role("link", name=product_name, exact=True))

    def product_price(self, product_name:str):
        return self.product_row(product_name).locator(".cart_price")

    def product_quantity(self, product_name:str):
        return self.product_row(product_name).locator(".cart_quantity")

    def product_total(self, product_name:str):
        return self.product_row(product_name).locator(".cart_total")
