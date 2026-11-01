from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(str(seconds))

    def press(self, button):
        self.driver.find_element(
            By.XPATH, f"//span[normalize-space()='{button}']"
        ).click()

    def wait_for_result(self, expected, timeout):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*self.result).text == expected
        )
        return self.driver.find_element(*self.result).text
