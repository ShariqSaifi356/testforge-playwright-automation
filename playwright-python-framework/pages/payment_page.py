from pages.base_page import BasePage


class PaymentPage(BasePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.payment_heading = page.get_by_role("heading", name="Payment", exact=True)
        self.name_on_card = page.locator("[data-qa='name-on-card']")
        self.card_number = page.locator("[data-qa='card-number']")
        self.cvc = page.locator("[data-qa='cvc']")
        self.expiry_month = page.locator("[data-qa='expiry-month']")
        self.expiry_year = page.locator("[data-qa='expiry-year']")
        self.pay_button = page.get_by_role("button", name="Pay and Confirm Order", exact=True)
        self.success_message = page.get_by_text("Your order has been placed successfully!", exact=True)
        self.order_placed_heading = page.get_by_role("heading", name="Order Placed!", exact=True)
        self.confirmation_message = page.get_by_text("Congratulations! Your order has been confirmed!", exact=True)
