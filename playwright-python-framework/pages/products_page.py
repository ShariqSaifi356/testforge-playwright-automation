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
