from decimal import Decimal
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_case_12(page, logger):

    home_page = HomePage(page, logger)
    products_page = ProductsPage(page, logger)
    cart_page = CartPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_products()
    expect(products_page.products_heading).to_be_visible()

    expected_products = []
    for index in range(2):
        product_name = products_page.inner_text(products_page.product_name(index)).strip()
        price_text = products_page.inner_text(products_page.product_price(index)).strip()
        price = Decimal(price_text.removeprefix("Rs.").replace(",", "").strip())
        expected_products.append((product_name, price_text, price))
        products_page.hover_product(index)
        products_page.click_add_to_cart(index)
        expect(products_page.continue_shopping_button).to_be_visible()
        if index == 0:
            products_page.click_continue_shopping()
            expect(products_page.continue_shopping_button).to_be_hidden()

    products_page.click_view_cart()
    logger.info("Verifying both products, prices, quantities and totals")
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    expect(cart_page.cart_heading).to_be_visible()
    expect(cart_page.product_rows).to_have_count(2)
    for product_name, price_text, price in expected_products:
        expect(cart_page.product_row(product_name)).to_be_visible()
        expect(cart_page.product_price(product_name)).to_have_text(price_text)
        expect(cart_page.product_quantity(product_name)).to_have_text("1")
        total_text = cart_page.inner_text(cart_page.product_total(product_name))
        total = Decimal(total_text.removeprefix("Rs.").replace(",", "").strip())
        assert total == price * 1, f"Incorrect total for {product_name}"
