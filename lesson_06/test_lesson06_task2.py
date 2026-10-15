from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def set_cookies(driver, cookies):
    # Selenium принимает cookie только для уже открытого домена.
    driver.get("https://gitflic.ru/")
    driver.delete_all_cookies()

    for cookie in cookies:
        cookie = {k: v for k, v in cookie.items()
                  if k in {
                            "name",
                            "value",
                            "domain",
                            "path",
                            "secure",
                            "httpOnly",
                            "sameSite",
                            "expiry",
                  }}
        driver.add_cookie(cookie)


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    # Замените примеры реальными cookie каждого аккаунта.
    tania26 = [
     {
        "name": "SESSION",
        "value": "NTUyNzA0NDEtYThiMC00YWQ1LWIyZWMtZTc0ZjhmYTRiNjQ5",
     }
    ]
    aleksis123 = [
     {
        "name": "SESSION",
        "value": "ZTNiZWZmMWUtNGM3OC00OWM0LTk0OTItNTEwYzY4NGZhODlm",
     }
    ]

    try:
        set_cookies(driver, tania26)
        driver.refresh()

        # Укажите URL профиля пользователя 1.
        driver.get("https://gitflic.ru/user/tania26")
        wait.until(
         lambda d: d.execute_script(
          "return document.readyState"
         ) == "complete"
        )
        user1_url = driver.current_url

        # Очистка cookie завершает текущую сессию.
        driver.delete_all_cookies()

        set_cookies(driver, aleksis123)
        driver.refresh()

        # Укажите URL профиля пользователя 2.
        driver.get("https://gitflic.ru/user/aleksis123")
        wait.until(
         lambda d: d.execute_script(
          "return document.readyState"
         ) == "complete"
        )
        user2_url = driver.current_url

        assert user1_url != user2_url, (
            f"URL профилей не различаются: {user1_url}"
        )
    finally:
        driver.quit()
