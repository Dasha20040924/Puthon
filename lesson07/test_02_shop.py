from decimal import Decimal

import pytest
from selenium import webdriver

from shop_page import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_saucedemo_checkout_total(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    for product in products:
        inventory_page.add_to_cart(product)

    inventory_page.open_cart()

    cart_page = CartPage(driver)
    assert set(cart_page.get_item_names()) == set(products)
    cart_page.checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info(
        first_name="Иван",
        last_name="Иванов",
        postal_code="123456",
    )
    checkout_page.continue_to_summary()

    assert checkout_page.get_total() == Decimal("58.29")
