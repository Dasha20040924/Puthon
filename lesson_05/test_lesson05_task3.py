from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        links = driver.find_elements(By.TAG_NAME, "a")

        assert len(links) == 9
        assert all(link.is_displayed() for link in links)
        assert "1" in links[0].text
    finally:
        driver.quit()
