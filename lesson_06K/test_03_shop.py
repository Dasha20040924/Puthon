from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop_checkout():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://www.saucedemo.com/")

        wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Дождаться, пока откроется каталог товаров
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for item in items:
            button_xpath = (
                "//div[contains(@class, 'inventory_item') "
                f"and .//*[contains(@class, 'inventory_item_name') "
                f"and normalize-space(.)='{item}']]//button"
            )
            wait.until(
                EC.element_to_be_clickable((By.XPATH, button_xpath))
            ).click()

        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys("Alex")
        driver.find_element(By.ID, "last-name").send_keys("Smith")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        total_text = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        ).text

        assert total_text == "Total: $58.29"

    finally:
        driver.quit()

