from socket import if_indextoname
import allure
from data import functions


@allure.suite("Test Suite 2. Customers — Сортировка по First Name")
@allure.title("TC_01 — Сортировка клиентов по убыванию")
@allure.severity(allure.severity_level.CRITICAL)
def test_sort_customers_descending(open_manager_page):

    page = open_manager_page

    with allure.step("Кликаем по кнопке Customers в меню"):

        page.click_on_customers_button_in_menu()

    with allure.step("Кликаем по надписи First Name в заголовке таблицы"):

        page.click_on_first_name_in_customers_table_header()

    with allure.step("Проверяем сортировку списка"):
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        if not functions.if_list_is_sorted_descendingly(customers, "First Name"):
            page.click_on_first_name_in_customers_table_header()
            headers_of_customers_table = page.get_list_of_headers_in_customers_table()
            list_of_customers = page.get_list_of_customers()
            customers = functions.generate_dict_of_customers(
                headers_of_customers_table, list_of_customers
            )

        assert functions.if_list_is_sorted_descendingly(
            customers, "First Name"
        ), "Сортировка клиентов по убыванию не корректна."


@allure.suite("Test Suite 2. Customers — Сортировка по First Name")
@allure.title("TC_02 — Сортировка клиентов по возрастанию")
@allure.severity(allure.severity_level.CRITICAL)
def test_sort_customers_ascending(open_manager_page):

    page = open_manager_page

    with allure.step("Кликаем по кнопке Customers в меню"):

        page.click_on_customers_button_in_menu()

    with allure.step("Кликаем по надписи First Name в заголовке таблицы"):

        page.click_on_first_name_in_customers_table_header()

    with allure.step("Проверяем сортировку списка"):
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        if functions.if_list_is_sorted_descendingly(customers, "First Name"):
            page.click_on_first_name_in_customers_table_header()
            headers_of_customers_table = page.get_list_of_headers_in_customers_table()
            list_of_customers = page.get_list_of_customers()
            customers = functions.generate_dict_of_customers(
                headers_of_customers_table, list_of_customers
            )

        assert not functions.if_list_is_sorted_descendingly(
            customers, "First Name"
        ), "Сортировка клиентов по возрастанию не корректна."


@allure.suite("Test Suite 2. Customers — Сортировка по First Name")
@allure.title("TC_03_N — Сортировка при одинаковых именах")
@allure.severity(allure.severity_level.NORMAL)
def test_sort_customers_with_same_first_name(open_manager_page):

    page = open_manager_page

    with allure.step(
        "Добавляем пользователя с именем, которое уже имеется в списке пользователей"
    ):

        page.click_on_customers_button_in_menu()
        customers = functions.generate_dict_of_customers(
            page.get_list_of_headers_in_customers_table(), page.get_list_of_customers()
        )
        first_name = functions.get_any_customer_credentials_from_customers(customers)

        page.click_on_add_customer_button_in_menu()
        postcode = page.fill_in_postcode()
        page.fill_in_first_name(postcode, first_name["First Name"])
        page.fill_in_last_name_field()
        page.click_on_add_customer_button_in_field()

        page.alert_ok()

    with allure.step("Проверяем сортировку списка"):
        page.click_on_customers_button_in_menu()
        page.click_on_first_name_in_customers_table_header()

        customers = functions.generate_dict_of_customers(
            page.get_list_of_headers_in_customers_table(), page.get_list_of_customers()
        )

        if functions.if_list_is_sorted_descendingly(customers, "First Name"):
            page.click_on_first_name_in_customers_table_header()
            headers_of_customers_table = page.get_list_of_headers_in_customers_table()
            list_of_customers = page.get_list_of_customers()
            customers = functions.generate_dict_of_customers(
                headers_of_customers_table, list_of_customers
            )

        assert not functions.if_list_is_sorted_descendingly(
            customers, "First Name"
        ), "Сортировка клиентов с дублем имени не корректна."
