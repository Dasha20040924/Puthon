from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.find(self.USERNAME).send_keys(username)
        self.find(self.PASSWORD).send_keys(password)
        self.click(self.LOGIN_BUTTON)


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, product_name):
        product_id = product_name.lower().replace(" ", "-")
        button = (By.CSS_SELECTOR, f'[data-test="add-to-cart-{product_id}"]')
        self.click(button)

    def open_cart(self):
        self.click(self.CART_LINK)


class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def get_item_names(self):
        items = self.wait.until(
            EC.presence_of_all_elements_located(self.CART_ITEMS)
        )
        return [
            item.find_element(By.CLASS_NAME, "inventory_item_name").text
            for item in items
        ]

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_customer_info(self, first_name, last_name, postal_code):
        self.find(self.FIRST_NAME).send_keys(first_name)
        self.find(self.LAST_NAME).send_keys(last_name)
        self.find(self.POSTAL_CODE).send_keys(postal_code)

    def continue_to_summary(self):
        self.click(self.CONTINUE_BUTTON)

    def get_total(self):
        total_text = self.find(self.TOTAL).text
        return Decimal(total_text.split("$")[1])
