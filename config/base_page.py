
import allure
from libs.helper import Helper
from data.links import Links
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Helper):
    PAGE_URL = Links.STAGE
    CONTACTS_TAB = "//a[text()='Contacts']"
    DASHBOARD_TAB = "//a[text()='Dashboard']"

    @allure.step("Открытие страницы, Open URL")
    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    @allure.step("Нажать на страницу контактов, Click on contact page")
    def go_to_contacts(self):
        self.wait_for_visibility(self.CONTACTS_TAB).click()

    @allure.step("Нажать на страницу дашборда, Click on dashboard page")
    def go_to_dashboard(self):
        self.wait_for_visibility(self.DASHBOARD_TAB).click()

