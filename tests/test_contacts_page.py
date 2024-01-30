import allure
import pytest

from config.base_test import BaseTest


@allure.feature("Contacts page")
class TestContactsPage(BaseTest):

    @allure.title("Add new contact")
    @pytest.mark.smoke
    def test_add_new_contact(self):
        self.base_page.open()
        self.base_page.go_to_contacts()
        self.contacts_page.is_opened()
        self.contacts_page.click_on_new_contact_button()
        self.contacts_page.add_first_name()
        self.contacts_page.add_last_name()
        self.contacts_page.add_title()
        self.contacts_page.add_email()
        self.contacts_page.select_manager()
        self.contacts_page.click_on_save_button()
        self.contacts_page.wait_confirmation()
        self.contacts_page.go_to_contacts()
        self.contacts_page.click_on_me_button()
        self.contacts_page.verify_contact_in_contact_list()

    @allure.title("Add node")
    def test_add_node(self):
        self.base_page.open()
        self.base_page.go_to_contacts()
        self.contacts_page.click_on_first_contact()
        self.contacts_page.add_note_in_contact_card()
        self.contacts_page.click_on_add_note_button()
        self.contacts_page.wait_confirmation_add_note()
        self.base_page.go_to_dashboard()
        self.contacts_page.find_note_on_dashboard()

    @allure.title("Add tag")
    def test_add_tag(self):
        self.base_page.open()
        self.base_page.go_to_contacts()
        self.contacts_page.click_on_mattie_beer()
        self.contacts_page.click_on_tags_in_contact_card()
        self.contacts_page.click_on_football_fan_tag_in_contact_card()
        self.base_page.go_to_contacts()
        self.contacts_page.click_on_football_fan_tag_on_contact_page()
        self.contacts_page.find_mattei_beer_in_contact_list_with_football_fans_tag()