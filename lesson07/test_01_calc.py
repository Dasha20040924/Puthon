import pytest
from selenium import webdriver

from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_calculator_addition_after_delay(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    for button in ("7", "+", "8", "="):
        page.press(button)

    assert page.wait_for_result("15", timeout=50) == "15"
