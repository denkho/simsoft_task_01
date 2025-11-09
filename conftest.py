import allure
import pytest
from selenium import webdriver

from pages.manager_page import ManagerPage
from config import Config


@pytest.fixture
def chrome_options():
    options = webdriver.ChromeOptions()

    if Config.HEADLESS:
        options.add_argument("--headless")
    if Config.INCOGNITO:
        options.add_argument("--incognito")
    if Config.START_MAXIMIZED:
        options.add_argument("--start-maximized")

    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-popup-blocking")
    return options


@pytest.fixture
def driver(chrome_options):
    print("\nStarting browser for tests...")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    yield driver

    print("\nQuiting browser...")
    driver.quit()


@pytest.fixture
def open_manager_page(driver) -> ManagerPage:
    page = ManagerPage(driver, Config.MANAGER_PAGE)
    page.open()
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG,
            )
