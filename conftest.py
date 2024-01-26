import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture(scope="function", autouse=True)
def driver(request):
    if os.environ["BROWSER"] == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
        action = ActionChains(driver)
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.quit()
    elif os.environ["BROWSER"] == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.quit()

