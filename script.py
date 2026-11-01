from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(5)
driver.quit()
python ui_first.py