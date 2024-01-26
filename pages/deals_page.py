import time
import allure
import random
from config.base_page import BasePage
from data.links import Links
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker


class DealsPage(BasePage):



    PAGE_URL = Links.DEALS_PAGE

    FIRST_OPPORTUNITY_CARD = "(//div[@data-rbd-droppable-id='opportunity']//div[@role='button'])[1]"
    PROPOSAL_COLLUM = "//div[@data-rbd-droppable-id='proposal-sent']"


    @allure.step("Перетаскивание")
    def drag_and_drop(self):
        first_opportunity_card = self.wait_for_clickable(self.FIRST_OPPORTUNITY_CARD)
        proposal_collum = self.wait_for_clickable(self.PROPOSAL_COLLUM)
        self.action.drag_and_drop(first_opportunity_card, proposal_collum).perform() # Перетаскиваем




























