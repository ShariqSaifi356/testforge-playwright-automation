from pages.base_page import BasePage


class ProductsPage(BasePage):

    def __init__(self, page, logger):
        super().__init__(page, logger)

        self.products_heading = page.get_by_role("heading", name="All Products", exact=True)
        self.products_list = page.locator(".features_items")
        self.product_cards = self.products_list.locator(".product-image-wrapper")
        self.product_names = self.product_cards.locator(".productinfo p")
        self.first_product_name = self.product_names.first
        self.first_view_product = self.product_cards.first.get_by_role("link", name="View Product")
        self.search_input = page.get_by_placeholder("Search Product", exact=True)
        self.search_button = page.locator("button#submit_search")
        self.searched_products_heading = page.get_by_role("heading", name="Searched Products", exact=True)

    def get_first_product_name(self):
        return self.inner_text(self.first_product_name)

    def click_first_view_product(self):
        self.click(self.first_view_product)

    def enter_search_product(self, product_name:str):
        self.fill(self.search_input, product_name)

    def click_search_button(self):
        self.wait_for_page_load()
        self.click(self.search_button)

    def product_card(self, index:int):
        return self.product_cards.nth(index)

    def product_name(self, index:int):
        return self.product_card(index).locator(".productinfo p")

    def product_price(self, index:int):
        return self.product_card(index).locator(".productinfo").get_by_role("heading", level=2)

    def add_to_cart_button(self, index:int):
        return self.product_card(index).locator(".product-overlay").get_by_text("Add to cart", exact=True)

    @property
    def continue_shopping_button(self):
        return self.page.get_by_role("button", name="Continue Shopping", exact=True)

    @property
    def view_cart_link(self):
        return self.page.get_by_role("link", name="View Cart", exact=True)

    def hover_product(self, index:int):
        self.wait_for_page_load()
        self.hover(self.product_card(index))

    def click_add_to_cart(self, index:int):
        self.click(self.add_to_cart_button(index))

    def click_continue_shopping(self):
        self.click(self.continue_shopping_button)

    def click_view_cart(self):
        self.click(self.view_cart_link)
