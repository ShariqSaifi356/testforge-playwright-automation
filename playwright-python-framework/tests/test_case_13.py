import re
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage
from pages.cart_page import CartPage


def test_case_13(page, logger):

    QUANTITY = "4"

    home_page = HomePage(page, logger)
    products_page = ProductsPage(page, logger)
    product_details_page = ProductDetailsPage(page, logger)
    cart_page = CartPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    product_name = products_page.get_first_product_name().strip()
    products_page.click_first_view_product()

    logger.info("Verifying product details and increasing quantity")
    expect(page).to_have_url(re.compile(r"https://automationexercise\.com/product_details/\d+/?$"))
    expect(product_details_page.product_details).to_be_visible()
    expect(product_details_page.product_name).to_have_text(product_name)
    product_details_page.enter_quantity(QUANTITY)
    expect(product_details_page.quantity).to_have_value(QUANTITY)
    product_details_page.click_add_to_cart()
    products_page.click_view_cart()

    logger.info("Verifying product is in cart with quantity 4")
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    expect(cart_page.cart_heading).to_be_visible()
    expect(cart_page.product_rows).to_have_count(1)
    expect(cart_page.product_row(product_name)).to_be_visible()
    expect(cart_page.product_quantity(product_name)).to_have_text(QUANTITY)
