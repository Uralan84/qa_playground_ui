from libs.helper import Helper
from pages.contacts_page import ContactsPage
from pages.deals_page import DealsPage
from config.base_page import BasePage


class BaseTest:



    def setup(self):
        self.helper = Helper(self.driver)
        self.base_page = BasePage(self.driver)
        self.contacts_page = ContactsPage(self.driver)
        self.deals_page = DealsPage(self.driver)

