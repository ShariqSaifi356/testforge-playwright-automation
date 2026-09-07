from pages.cart_page import CartPage


class CheckoutPage(CartPage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.address_details_heading = page.get_by_role("heading", name="Address Details", exact=True)
        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")
        self.review_order_heading = page.get_by_role("heading", name="Review Your Order", exact=True)
        self.total_amount = self.cart_table.get_by_role("row").filter(has_text="Total Amount").locator(".cart_total_price")
        self.comment = page.locator("textarea[name='message']")
        self.place_order_link = page.get_by_role("link", name="Place Order", exact=True)
