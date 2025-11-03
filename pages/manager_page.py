from selenium.webdriver.chrome.webdriver import WebDriver

from pages import locators
import data.functions
from pages.base_page import BasePage


class ManagerPage(BasePage):
    def __init__(self, driver: WebDriver, url: str):
        super().__init__(driver, url)

    def click_on_add_customer_button_in_menu(self):
        self.click(locators.ManagerPage.BUTTON_ADD_CUSTOMER)

    def fill_in_postcode(self, postcode=None):
        if postcode is None:
            postcode = data.functions.postcode_generator()
        self.fill_in_input_field(locators.ManagerPage.FIELD_POST_CODE, postcode)
        return postcode

    def fill_in_first_name(self, postcode, first_name=None):
        if first_name is None:
            first_name = data.functions.postcode_to_name(postcode)
        self.fill_in_input_field(locators.ManagerPage.FIELD_FIRST_NAME, first_name)
        return first_name

    def fill_in_last_name_field(self, last_name=None):
        if last_name is None:
            last_name = data.functions.generate_last_name()
        self.fill_in_input_field(locators.ManagerPage.FIELD_LAST_NAME, last_name)
        return last_name

    def click_on_add_customer_button_in_field(self):
        self.click(locators.ManagerPage.BUTTON_ADD_CUSTOMER_FIELD)

    def click_on_customers_button_in_menu(self):
        self.click(locators.ManagerPage.BUTTON_CUSTOMERS)

    def get_list_of_headers_in_customers_table(self):
        return self.get_list_of_objects(locators.ManagerPage.HEADERS_OF_CUSTOMERS_TABLE)

    def get_list_of_customers(self):
        return self.get_list_of_objects(locators.ManagerPage.CUSTOMERS_INFO)

    def click_on_first_name_in_customers_table_header(self):
        self.click(locators.ManagerPage.TABLE_HEADER_FIRST_NAME)

    def delete_customer_by_name(self, first_name, last_name):
        locator_xpath_of_button = data.functions.generate_delete_button_xpath(
            first_name, last_name
        )
        self.click(("xpath", locator_xpath_of_button))

    def click_delete_button(self):
        self.click(locators.ManagerPage.BUTTON_DELETE_CUSTOMER)

    def check_if_delete_button_is_absent(self):
        return self.element_is_absent(locators.ManagerPage.BUTTON_DELETE_CUSTOMER)
