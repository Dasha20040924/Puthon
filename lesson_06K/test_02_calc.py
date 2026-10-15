from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_slow_calculator():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

        for button in ("7", "+", "8", "="):
            driver.find_element(
                By.XPATH, f"//span[normalize-space()='{button}']"
            ).click()

        result = WebDriverWait(driver, 50).until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".screen").text == "15"
        )
        print(result.text) 
        assert result
    finally:
        driver.quit()
