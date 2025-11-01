from selenium.webdriver.chrome.webdriver import WebDriver

from pages import locators
import data.functions
from pages.base_page import BasePage


class ManagerPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    def click_on_add_customer_button_in_menu(self):
        self.click(locators.ManagerPage.BUTTON_ADD_CUSTOMER)

    def fill_in_first_name_field_and_postcode_field(self):
        postcode = data.functions.postcode_generator()
        first_name = data.functions.postcode_to_name(postcode)
        self.fill_in_input_field(locators.ManagerPage.FIELD_POST_CODE, postcode)
        self.fill_in_input_field(locators.ManagerPage.FIELD_FIRST_NAME, first_name)

    def fill_in_last_name_field(self):
        last_name = data.functions.generate_last_name()
        self.fill_in_input_field(locators.ManagerPage.FIELD_LAST_NAME, last_name)
    

    def click_on_add_customer_button_in_field(self):
        self.click(locators.ManagerPage.BUTTON_ADD_CUSTOMER_FIELD)
