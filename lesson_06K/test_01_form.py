from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_form():
    driver = webdriver.Edge()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait = WebDriverWait(driver, 30)
        wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        values = {
            "First name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for field_id, value in values.items():
            driver.find_element(By.ID, field_id).send_keys("First name")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class")

        for field_id in values:
            field = driver.find_element(By.ID, field_id)
            assert "alert-success" in field.get_attribute("class")

    finally:
        driver.quit()

