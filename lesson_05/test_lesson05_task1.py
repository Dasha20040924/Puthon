from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    try:
        start_url = "https://httpbin.qa-territory.online"
        driver.get(start_url)

        driver.find_element(By.LINK_TEXT, "HTML Form").click()
        assert driver.current_url.rstrip("/").endswith("/forms/post")

        driver.back()
        assert driver.current_url.rstrip("/") == start_url.rstrip("/")
    finally:
        driver.quit()
