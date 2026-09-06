import re
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_details_page import ProductDetailsPage


def test_case_8(page, logger):

    home_page = HomePage(page, logger)
    products_page = ProductsPage(page, logger)
    product_details_page = ProductDetailsPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_products()

    logger.info("Verifying 'All Products' page")
    expect(page).to_have_url("https://automationexercise.com/products")
    expect(products_page.products_heading).to_be_visible()
    expect(products_page.products_heading).to_have_text("All Products")
    expect(products_page.products_list).to_be_visible()
    expect(products_page.first_product_name).to_be_visible()
    product_name = products_page.get_first_product_name()
    products_page.click_first_view_product()

    logger.info("Verifying product detail page")
    expect(page).to_have_url(re.compile(r"https://automationexercise\.com/product_details/\d+/?$"))
    expect(product_details_page.product_details).to_be_visible()
    expect(product_details_page.product_name).to_be_visible()
    expect(product_details_page.product_name).to_have_text(product_name)
    expect(product_details_page.category).to_be_visible()
    expect(product_details_page.price).to_be_visible()
    expect(product_details_page.availability).to_be_visible()
    expect(product_details_page.condition).to_be_visible()
    expect(product_details_page.brand).to_be_visible()
