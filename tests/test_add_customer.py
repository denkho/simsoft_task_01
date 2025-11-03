from functools import partial
import allure
import random
from data import functions
from data.data import Data


@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_01 — Успешное добавление клиента")
@allure.severity(allure.severity_level.BLOCKER)
def test_add_customer_positive(open_manager_page):

    page = open_manager_page

    with allure.step("Кликаем по кнопке Add Customer в меню"):
        page.click_on_add_customer_button_in_menu()

    with allure.step("Заполняем поля клиента и кликаем по кнопке Add Customer"):
        postcode = page.fill_in_postcode()
        first_name = page.fill_in_first_name(postcode)
        last_name = page.fill_in_last_name_field()
        page.click_on_add_customer_button_in_field()

        alert_text = page.get_alert_text()
        page.alert_ok()

    with allure.step("Проверяем, что появился Alert с корректным сообщением"):
        assert alert_text.startswith(
            Data.ALERT_TEXT_FOR_CUSTOMER_ADD_SUCCESSFUL
        ), f"Отсутсвует alert или его текст изменился. \
            Текст Alert должен начинаться с {Data.ALERT_TEXT_FOR_CUSTOMER_ADD_SUCCESSFUL}, \
            а содержит {alert_text}"

    with allure.step("Переходим в список клиентов"):

        page.click_on_customers_button_in_menu()

        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

    with allure.step("Проверяем, что клиент содержится в списке"):
        assert functions.find_customer_in_list_of_customers(
            customers, first_name, last_name, postcode
        ), f"Отсутствует клиент с {first_name}, {last_name} и {postcode}"


@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_02_N — Добавление клиента с пустыми полями")
@allure.severity(allure.severity_level.NORMAL)
def test_add_customer_without_filling_the_required_fields(open_manager_page):
    page = open_manager_page

    with allure.step(
        "Переходим в список клиентов и сохраняем его для последующей проверки"
    ):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

    with allure.step(
        "Переходим на вкладку Add Customer для добавления клиента без заполнения полей"
    ):
        page.click_on_add_customer_button_in_menu()
        page.click_on_add_customer_button_in_field()

    with allure.step("Проверяем отсутствие Allert"):
        assert not page.is_alert_present(), "Alert отобразился на странице"

    with allure.step("Проверяем, что список клиентов не изменился"):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers_to_check = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        assert len(customers) == len(
            customers_to_check
        ), f"Список клиентов содержал {len(customers)} клиентов, \
            теперь стал содержать {len(customers_to_check)}"


@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_03_N — Добавление клиента через заполнение одного обязательного поля")
@allure.severity(allure.severity_level.NORMAL)
def test_add_customer_with_fill_only_one_required_field(open_manager_page):
    page = open_manager_page

    with allure.step(
        "Переходим в список клиентов и сохраняем его для последующей проверки"
    ):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

    with allure.step(
        "Переходим на вкладку Add Customer для добавления клиента и заполняем случайным образом одно из полей"
    ):
        page.click_on_add_customer_button_in_menu()
        postcode = functions.postcode_generator()
        methods = [
            partial(page.fill_in_first_name, postcode),
            page.fill_in_last_name_field,
            partial(page.fill_in_postcode, postcode),
        ]
        random.choice(methods)()
        page.click_on_add_customer_button_in_field()

    with allure.step("Проверяем отсутствие Allert"):
        assert not page.is_alert_present(), "Alert отобразился на странице"

    with allure.step("Проверяем, что список клиентов не изменился"):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers_to_check = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        assert len(customers) == len(
            customers_to_check
        ), f"Список клиентов содержал {len(customers)} клиентов, \
            теперь стал содержать {len(customers_to_check)}"


@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_04_N — Добавление клиента с одним незаполненным полем")
@allure.severity(allure.severity_level.NORMAL)
def test_add_customer_with_fill_of_two_required_field(open_manager_page):
    page = open_manager_page

    with allure.step(
        "Переходим в список клиентов и сохраняем его для последующей проверки"
    ):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

    with allure.step(
        "Переходим на вкладку Add Customer для добавления клиента и заполняем случайным образом два из полей"
    ):
        page.click_on_add_customer_button_in_menu()
        postcode = functions.postcode_generator()
        methods = [
            partial(page.fill_in_first_name, postcode),
            page.fill_in_last_name_field,
            partial(page.fill_in_postcode, postcode),
        ]
        methods_to_do = random.sample(methods, 2)
        for el in methods_to_do:
            el()
        page.click_on_add_customer_button_in_field()

    with allure.step("Проверяем отсутствие Allert"):
        assert not page.is_alert_present(), "Alert отобразился на странице"

    with allure.step("Проверяем, что список клиентов не изменился"):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers_to_check = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        assert len(customers) == len(
            customers_to_check
        ), f"Список клиентов содержал {len(customers)} клиентов, \
            теперь стал содержать {len(customers_to_check)}"


@allure.suite("Test Suite 1. Создание клиента (Add Customer)")
@allure.title("TC_05_N — Добавление дублирующегося клиента")
@allure.severity(allure.severity_level.NORMAL)
def test_add_customer_with_the_same_credentials(open_manager_page):
    page = open_manager_page

    with allure.step("Генерируем имя и фамилию клиента с почтовым кодом"):
        postcode = functions.postcode_generator()
        first_name = functions.postcode_to_name(postcode)
        last_name = functions.generate_last_name()

    with allure.step(
        "Переходим на вкладку Add Customer для добавления клиента и заполняем поля"
    ):
        page.click_on_add_customer_button_in_menu()
        page.fill_in_first_name(postcode, first_name)
        page.fill_in_last_name_field(last_name)
        page.fill_in_postcode(postcode)
        page.click_on_add_customer_button_in_field()
        page.alert_ok()

    with allure.step(
        "Переходим в список клиентов и сохраняем его для последующей проверки"
    ):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

    with allure.step(
        "Переходим повторно на вкладку Add Customer заполняем поля теми же данными"
    ):
        page.click_on_add_customer_button_in_menu()

        page.fill_in_first_name(postcode, first_name)
        page.fill_in_last_name_field(last_name)
        page.fill_in_postcode(postcode)

        page.click_on_add_customer_button_in_field()

    with allure.step("Проверяем, что появился Alert с корректным сообщением"):
        alert_text = page.get_alert_text()
        page.alert_ok()
        assert (
            alert_text == Data.ALERT_TEXT_FOR_CUSTOMER_DUPLICATE
        ), f"Отсутсвует alert или его текст изменился. \
            Текст Alert должен содержать {Data.ALERT_TEXT_FOR_CUSTOMER_DUPLICATE}, \
            а содержит {alert_text}"

    with allure.step("Проверяем, что список клиентов не изменился"):
        page.click_on_customers_button_in_menu()
        headers_of_customers_table = page.get_list_of_headers_in_customers_table()
        list_of_customers = page.get_list_of_customers()
        customers_to_check = functions.generate_dict_of_customers(
            headers_of_customers_table, list_of_customers
        )

        assert len(customers) == len(
            customers_to_check
        ), f"Список клиентов содержал {len(customers)} клиентов, \
            теперь стал содержать {len(customers_to_check)}"
