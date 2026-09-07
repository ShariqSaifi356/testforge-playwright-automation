import re
from decimal import Decimal
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage


def test_case_14(page, logger):

    NAME = "Arpita"
    EMAIL = f"arpita{__import__('uuid').uuid4().hex}@example.com"
    PASSWORD = "AaBb123@123SaaS"
    DAY = "6"
    MONTH = "11"
    YEAR = "1998"
    FIRST_NAME = "Arpit"
    LAST_NAME = "Singh"
    COMPANY = "ImpactQA"
    ADDRESS = "69A, Sector 10A, Gurgaon"
    ADDRESS_2 = "India"
    COUNTRY = "India"
    STATE = "HR"
    CITY = "Gurgaon"
    ZIPCODE = "120001"
    MOBILE_NUMBER = "9000000001"
    COMMENT = "Please deliver this test order carefully."
    NAME_ON_CARD = "Test Customer"
    CARD_NUMBER = "4111111111111111"
    CVC = "123"
    EXPIRY_MONTH = "12"
    EXPIRY_YEAR = str(__import__('datetime').date.today().year + 2)

    home_page = HomePage(page, logger)
    products_page = ProductsPage(page, logger)
    cart_page = CartPage(page, logger)
    signup_page = SignupPage(page, logger)
    login_page = LoginPage(page, logger)
    checkout_page = CheckoutPage(page, logger)
    payment_page = PaymentPage(page, logger)

    home_page.navigate("http://automationexercise.com/")
    logger.info("Verifying home page")
    expect(home_page.home_page_element).to_be_visible()
    expect(home_page.features_heading).to_be_visible()

    expected_products = []
    for index in range(2):
        product_name = products_page.inner_text(products_page.product_name(index)).strip()
        price_text = products_page.inner_text(products_page.product_price(index)).strip()
        price = Decimal(price_text.removeprefix("Rs.").replace(",", "").strip())
        expected_products.append((product_name, price_text, price))
        products_page.hover_product(index)
        products_page.click_add_to_cart(index)
        expect(products_page.continue_shopping_button).to_be_visible()
        products_page.click_continue_shopping()
        expect(products_page.continue_shopping_button).to_be_hidden()
    home_page.click_cart()
    expect(page).to_have_url("https://automationexercise.com/view_cart")
    expect(cart_page.cart_heading).to_be_visible()
    expect(cart_page.product_rows).to_have_count(2)
    cart_page.wait_for_page_load()
    cart_page.click(cart_page.proceed_to_checkout)

    expect(cart_page.register_login_link).to_be_visible()
    cart_page.click(cart_page.register_login_link)

    logger.info("Creating a new account")
    expect(signup_page.signup_heading).to_be_visible()
    signup_page.enter_name(NAME)
    signup_page.enter_signup_email(EMAIL)
    signup_page.click_signup_button()
    expect(signup_page.signup_heading_2).to_be_visible()
    signup_page.select_title()
    signup_page.enter_password(PASSWORD)
    signup_page.select_day(DAY)
    signup_page.select_month(MONTH)
    signup_page.select_year(YEAR)
    signup_page.select_newsletter()
    signup_page.select_specialoffers()
    expect(signup_page.signup_heading_3).to_be_visible()
    signup_page.enter_first_name(FIRST_NAME)
    signup_page.enter_last_name(LAST_NAME)
    signup_page.enter_company(COMPANY)
    signup_page.enter_address(ADDRESS)
    signup_page.enter_address_2(ADDRESS_2)
    signup_page.select_country(COUNTRY)
    signup_page.select_state(STATE)
    signup_page.enter_city(CITY)
    signup_page.enter_zip_code(ZIPCODE)
    signup_page.enter_mobile_number(MOBILE_NUMBER)
    signup_page.click_create_account()
    expect(signup_page.signup_heading_4).to_be_visible()
    expect(signup_page.signup_heading_4).to_have_text("Account Created!")
    signup_page.click_continue()
    expect(login_page.logged_in_username).to_be_visible()
    expect(login_page.username_visible).to_have_text(NAME)

    home_page.click_cart()
    expect(cart_page.cart_heading).to_be_visible()
    cart_page.wait_for_page_load()
    cart_page.click(cart_page.proceed_to_checkout)

    logger.info("Verifying address details and review of the order")
    expect(page).to_have_url("https://automationexercise.com/checkout")
    expect(checkout_page.address_details_heading).to_be_visible()
    expected_address = [
        f"Mr. {FIRST_NAME} {LAST_NAME}", COMPANY, ADDRESS, ADDRESS_2,
        f"{CITY} {STATE} {ZIPCODE}", COUNTRY, MOBILE_NUMBER
    ]
    for address in (checkout_page.delivery_address, checkout_page.billing_address):
        expect(address).to_be_visible()
        for line in expected_address:
            expect(address).to_contain_text(line)
    expect(checkout_page.review_order_heading).to_be_visible()
    expect(checkout_page.product_rows).to_have_count(2)
    for product_name, price_text, price in expected_products:
        expect(checkout_page.product_row(product_name)).to_be_visible()
        expect(checkout_page.product_price(product_name)).to_have_text(price_text)
        expect(checkout_page.product_quantity(product_name)).to_have_text("1")
        total_text = checkout_page.inner_text(checkout_page.product_total(product_name))
        assert Decimal(total_text.removeprefix("Rs.").replace(",", "").strip()) == price
    order_total = checkout_page.inner_text(checkout_page.total_amount)
    assert Decimal(order_total.removeprefix("Rs.").replace(",", "").strip()) == sum(
        price for _, _, price in expected_products
    )
    checkout_page.fill(checkout_page.comment, COMMENT)
    expect(checkout_page.comment).to_have_value(COMMENT)
    checkout_page.click(checkout_page.place_order_link)

    logger.info("Entering dummy payment details on the practice website")
    expect(payment_page.payment_heading).to_be_visible()
    payment_page.fill(payment_page.name_on_card, NAME_ON_CARD)
    payment_page.fill(payment_page.card_number, CARD_NUMBER)
    payment_page.fill(payment_page.cvc, CVC)
    payment_page.fill(payment_page.expiry_month, EXPIRY_MONTH)
    payment_page.fill(payment_page.expiry_year, EXPIRY_YEAR)
    payment_page.click(payment_page.pay_button)

    logger.info("Verifying the live site's visible order confirmation")
    expect(page).to_have_url(re.compile(r"https://automationexercise\.com/payment_done/\d+/?$"))
    expect(payment_page.order_placed_heading).to_be_visible()
    expect(payment_page.confirmation_message).to_be_visible()
    expect(payment_page.confirmation_message).to_have_text("Congratulations! Your order has been confirmed!")
