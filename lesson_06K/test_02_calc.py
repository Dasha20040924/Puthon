import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TestSlowCalculator(unittest.TestCase):
    def test_slow_calculator(self):
        driver = webdriver.Chrome()

        try:
            driver.get(
               (
                  "https://bonigarcia.dev/selenium-webdriver-java/"
                   "slow-calculator.html"
               )
            )

            delay = driver.find_element(By.CSS_SELECTOR, "#delay")
            delay.clear()
            delay.send_keys("45")

            for button in ("7", "+", "8", "="):
                driver.find_element(
                    By.XPATH, f"//span[normalize-space()='{button}']"
                ).click()

            result = WebDriverWait(driver, 60).until(
                lambda d: (
                 d.find_element(By.CSS_SELECTOR, ".screen").text
                 == "15"
                )
            )
            self.assertTrue(result)
        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()

