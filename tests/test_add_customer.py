import allure

from data.data import Data

@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_01 — Успешное добавление клиента")
def test_add_customer_positive(open_manager_page):
    page = open_manager_page

    page.click_on_add_customer_button_in_menu()
    page.fill_in_first_name_field_and_postcode_field()
    page.fill_in_last_name_field()
    page.click_on_add_customer_button_in_field()

    alert_text = page.get_alert_text()

    assert alert_text.startswith(Data.ALERT_TEXT_FOR_CUSTOMER_ADD_SUCCESSFUL), "Отсутсвует alert или его текст изменился"
    