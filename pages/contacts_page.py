import time

import allure
import random
from config.base_page import BasePage
from data.links import Links
from faker import Faker


class ContactsPage(BasePage):

    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    note = fake.text()

    PAGE_URL = Links.CONTACTS_PAGE

    NEW_CONTACT_BUTTON = "//a[@aria-label='New Contact']"
    FIRST_NAME_FIELD = "//input[@id='first_name']"
    LAST_NAME_FIELD = "//input[@id='last_name']"
    TITLE_FIELD = "//input[@id='title']"
    EMAIL_FIELD = "//input[@id='email']"
    ACCOUNT_MANAGER_DROPDOWN = "//div[@id='sales_id']"
    FIRST_MANAGER = "//ul[@aria-labelledby='sales_id-label']//li[2]"
    SAVE_BUTTON = "//button[@type='submit']"
    ELEMENT_CREATED_TEXT = "//div[text()='Element created']"
    ME_BUTTON = "//span[text()='Me']"
    FIRST_CONTACT = "(//li[contains(@class, 'container')])[1]"
    ADD_NODE_FIELD = "//textarea[1]"
    ADD_NODE_BUTTON = "//button[@type='submit']"
    NODE_ADDED_ALERT = "//div[text()='Note added successfully']"
    ADD_TAG_BUTTON = "//span[text()='Add tag']"
    FOOTBALL_FAN_TAG = "//div[@role='button']//span[text()='football-fan']"
    MATTIE_BEER = "//span[text()='Mattie Beer']"
    CONTACT_LIST_WITH_FOOTBALL_FAN_TAG = "//span[contains(@class,'css-yb0lig')]"
    # get_first_name = lambda first_name: ("xpath", f"//span[contains(text(),'{first_name}')]")
    @staticmethod
    def get_first_name(first_name):
        return (f"//span[contains(text(),'{first_name}')]")

    @staticmethod
    def get_note_in_contact_card(note):
        return (f"//p[text()='{note}']")

    @staticmethod
    def get_note_on_dashboard(note):
        return (f"//p[text()='{note}']")


    @allure.step("Проверка открытия страницы контактов, Open contacts page URL")
    def contacts_page_is_opened(self):
        self.is_opened(self.PAGE_URL)

    @allure.step("Нажать на кнопку New Contact, Click on new contact button")
    def click_on_new_contact_button(self):
        self.wait_for_clickable(self.NEW_CONTACT_BUTTON).click()

    @allure.step("Ввод имени, Add first name")
    def add_first_name(self):
        self.first_name_field = self.wait_for_clickable(self.FIRST_NAME_FIELD)
        self.first_name_field.send_keys(self.first_name)
        assert self.first_name_field.get_attribute("value") == self.first_name, "Отображается неверное имя"

    @allure.step("Ввод фамилии, Add last name")
    def add_last_name(self):
        self.last_name_field = self.wait_for_clickable(self.LAST_NAME_FIELD)
        self.last_name_field.send_keys(self.last_name)
        assert self.last_name_field.get_attribute("value") == self.last_name, "Отображается неверная фамилия"

    @allure.step("Ввод описания контакта, Add title")
    def add_title(self):
        self.title_field = self.wait_for_clickable(self.TITLE_FIELD)
        self.title_field.send_keys('description')
        assert self.title_field.get_attribute("value") == 'description', "Отображается неверное описание контакта"

    @allure.step("Ввод электронной почты, Add email")
    def add_email(self):
        self.email_field = self.wait_for_clickable(self.EMAIL_FIELD)
        self.email_field.send_keys(self.email)
        assert self.email_field.get_attribute("value") == self.email, "Отображается неверная электронная почта"


    @allure.title("Выбрать менеджера, Select manager")
    def select_manager(self):
        self.wait_for_clickable(self.ACCOUNT_MANAGER_DROPDOWN).click()
        self.wait_for_clickable(self.FIRST_MANAGER).click()
        account_manager_dropdown_full = self.wait_for_visibility(self.ACCOUNT_MANAGER_DROPDOWN)
        assert account_manager_dropdown_full.get_attribute("value") != " ", "Менеджер не выбран"

    @allure.step("Нажать на кнопку Сохранить, Click on Save button")
    def click_on_save_button(self):
        self.wait_for_clickable(self.SAVE_BUTTON).click()

    @allure.step("Дождаться появления подтверждения добавления контакта, Wait for confirmation to appear")
    def wait_confirmation(self):
        assert self.wait_for_visibility(self.ELEMENT_CREATED_TEXT), "Уведомление о добавлении контакта не появилось"

    @allure.step("Нажать на кнопку Me, Click on Me button")
    def click_on_me_button(self):
        self.wait_for_clickable(self.ME_BUTTON).click()

    @allure.title("Найти добавленный контакт в списке контактов, Find an added contact in contact list")
    def verify_contact_in_contact_list(self):
        assert self.wait_for_visibility(self.get_first_name(self.first_name)), "Контакт не добавился в список контактов"

    @allure.step("Нажать на первый контакт в списке, Click on the first contact in the list")
    def click_on_first_contact(self):
        self.wait_for_clickable(self.FIRST_CONTACT).click()

    @allure.step("Ввести заметку в карточку контакта, Enter a node")
    def add_note_in_contact_card(self):
        self.add_note_field = self.wait_for_clickable(self.ADD_NODE_FIELD)
        self.add_note_field.send_keys(self.note)

    @allure.step("Нажать на кнопку Добавить заметку, Click on add this note button")
    def click_on_add_note_button(self):
        self.wait_for_clickable(self.ADD_NODE_BUTTON).click()

    @allure.step("Дождаться появления подтверждения добавления заметки, Wait for confirmation to add a note")
    def wait_confirmation_add_note(self):
        assert self.wait_for_visibility(self.NODE_ADDED_ALERT), "Уведомление о добавлении заметки не появилось"

    @allure.title("Найти добавленную заметку в карточке контакта, Find added note in contact card")
    def find_note_in_contact_card(self):
        assert self.wait_for_visibility(self.get_note_in_contact_card(self.note)), "Заметка не добавилась в карточку контакта"

    @allure.step("Нажать на Mattie Beer, Click on Mattie Beer")
    def click_on_mattie_beer(self):
        self.wait_for_clickable(self.MATTIE_BEER).click()

    @allure.title("Нажать на кнопку tags в карточке контакта, Click on the tags button in the contact card")
    def click_on_tags_in_contact_card(self):
        self.wait_for_clickable(self.ADD_TAG_BUTTON).click()

    @allure.title("Нажать на тег football-fan в карточке контакта, Click on the football fan tag in the contact card")
    def click_on_football_fan_tag_in_contact_card(self):
        self.wait_for_clickable(self.FOOTBALL_FAN_TAG).click()

    @allure.title("Нажать на тег football-fan в странице контактов, Click on the tags button in the contact page")
    def click_on_football_fan_tag_on_contact_page(self):
        self.wait_for_clickable(self.FOOTBALL_FAN_TAG).click()


    @allure.step("Найти Mattie Beer среди контактов с тегом football-fans, Find Mattie Beer among contacts tagged football-fans")
    def find_mattei_beer_in_contact_list_with_football_fans_tag(self):
        contact_list = []
        contacts = self.finds(self.CONTACT_LIST_WITH_FOOTBALL_FAN_TAG)
        for contact in contacts:
            contact_list.append(contact.text)
        assert "Mattie Beer" in contact_list, "Mattie Beer не получил тег football-fans"
































