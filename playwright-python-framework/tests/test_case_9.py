import re
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage


def test_case_9(page, logger):

    home_page = HomePage(page, logger)
    products_page = ProductsPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()
    home_page.click_products()

    logger.info("Verifying 'All Products' page")
    expect(page).to_have_url("https://automationexercise.com/products")
    expect(products_page.products_heading).to_be_visible()
    expect(products_page.products_heading).to_have_text("All Products")
    expect(products_page.first_product_name).to_be_visible()
    product_name = products_page.get_first_product_name()
    products_page.enter_search_product(product_name)
    products_page.click_search_button()

    logger.info("Verifying 'Searched Products' heading")
    expect(products_page.searched_products_heading).to_be_visible()
    expect(products_page.searched_products_heading).to_have_text("Searched Products")
    expect(products_page.first_product_name).to_be_visible()

    logger.info("Verifying every search result is visible and related to the search")
    for result_name in products_page.product_names.all():
        expect(result_name).to_be_visible()
        expect(result_name).to_contain_text(re.compile(re.escape(product_name), re.IGNORECASE))
