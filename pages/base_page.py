from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException


class BasePage:

    TIMEOUT = 10

    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=TIMEOUT):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=TIMEOUT):
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def element_is_clickable(self, locator, timeout=TIMEOUT):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def fill_in_input_field(self, locator, data):
        self.element_is_visible(locator).send_keys(data)

    def click(self, locator):
        self.element_is_clickable(locator).click()

    def select(self, locator, value):
        Select(self.element_is_clickable(locator)).select_by_value(value)

    def scroll_to_element(self, locator, smooth=False, position="center"):
        element = wait(self.driver, 10).until(EC.presence_of_element_located(locator))

        if smooth:
            script = f"arguments[0].scrollIntoView({{behavior: 'smooth', block: '{position}'}});"
        else:
            script = f"arguments[0].scrollIntoView({{block: '{position}'}});"

        self.driver.execute_script(script, element)
        return element

    def scroll_to_and_click(self, locator):
        element = self.scroll_to_element(locator)
        wait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def get_alert_text(self, timeout=10):
        wait(self.driver, timeout).until(EC.alert_is_present())
        return Alert(self.driver).text

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert 
            return True
        except NoAlertPresentException:
            return False
        
    def alert_ok(self):
        Alert(self.driver).accept()
        
    def get_list_of_objects(self, locator):
        return self.elements_are_visible(locator)
    