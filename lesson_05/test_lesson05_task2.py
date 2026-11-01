from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://httpbin.qa-territory.online/forms/post")
        original_url = driver.current_url

        name_field = wait.until(
            EC.visibility_of_element_located((By.NAME, "custname"))
        )
        name_field.send_keys("Дарья")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "input[type='submit'], button[type='submit']",
                )
            )
        )
        submit_button.click()

        wait.until(EC.url_changes(original_url))
        assert driver.current_url != original_url
    finally:
        driver.quit()
