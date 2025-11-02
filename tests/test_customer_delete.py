import allure

from data import functions


@allure.suite("Test Suite 3. Customers — Удаление клиента")
@allure.title("TC_01 — Успешное удаление клиента")
@allure.severity(allure.severity_level.CRITICAL)
def test_customer_delete(open_manager_page):

    page = open_manager_page

    with allure.step("Кликаем по кнопке Customers в меню"):

        page.click_on_customers_button_in_menu()

    with allure.step("Выбираем клиента для удаления"):
        customers = functions.generate_dict_of_customers(
            page.get_list_of_headers_in_customers_table(),
            page.get_list_of_customers(),
        )
        customer_to_delete = functions.get_any_customer_credentials_from_customers(
            customers
        )

    with allure.step("Удаляем выбранного клиента"):
        page.delete_customer_by_name(
            customer_to_delete["First Name"], customer_to_delete["Last Name"]
        )

    with allure.step("Проверяем наличие удаленного клиента в списке клиентов"):
        customers = functions.generate_dict_of_customers(
            page.get_list_of_headers_in_customers_table(),
            page.get_list_of_customers(),
        )

        assert not functions.find_customer_in_list_of_customers(
            customers,
            customer_to_delete["First Name"],
            customer_to_delete["Last Name"],
            customer_to_delete["Post Code"],
        ), f"Клиент с именем {customer_to_delete["First Name"] + " " + customer_to_delete["Last Name"],} не удален из списка"


@allure.suite("Test Suite 3. Customers — Удаление клиента")
@allure.title("TC_02_N — Удаление при пустом списке")
@allure.severity(allure.severity_level.MINOR)
def test_customer_delete_if_list_of_customers_empty(open_manager_page):

    page = open_manager_page

    with allure.step("Удаляем всех клиентов"):

        page.click_on_customers_button_in_menu()
        while not (page.check_if_delete_button_is_absent()):
            page.click_delete_button()

        assert (
            page.check_if_delete_button_is_absent()
        ), "Кнопка Delete в таблице присутствует"
