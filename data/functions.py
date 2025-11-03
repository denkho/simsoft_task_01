import random
from faker import Faker


def postcode_generator() -> str:
    return str(random.randint(10**9, 10**10 - 1))


def postcode_to_name(postcode) -> str:
    """
    Преобразует почтовый код в имя по следующему алгоритму:
    1) Post Code условно разбиваем на двузначные цифры (получится 5 цифр)
    2) Каждую цифру преобразовываем в букву английского алфавита по порядку от 0 до 25 .
    Если цифра больше 25 , то начинаем с 26 как с 0 . Т.е . 0 a, 26 тоже a, 52 тоже a, и т.д.
    Пример: 0001252667 = abzap

    Args:
        postcode (str): Почтовый код (10 цифр)

    Returns:
        str: Сгенерированное имя
    """

    two_digit_numbers = []
    for i in range(0, 10, 2):
        two_digit_numbers.append(int(postcode[i : i + 2]))

    # Преобразуем каждую цифру в букву
    name_letters = []
    for number in two_digit_numbers:
        normalized_number = number % 26
        letter = chr(ord("a") + normalized_number)
        name_letters.append(letter)

    name = "".join(name_letters).capitalize()

    return name


def generate_last_name() -> str:
    return Faker().last_name()


def generate_raw_list_of_text_from_objects(elements):
    return [element.text for element in elements]


def generate_dict_of_customers(k, v) -> dict:
    k = generate_raw_list_of_text_from_objects(k)
    v = generate_raw_list_of_text_from_objects(v)
    return [dict(zip(k, v[i : i + 3])) for i in range(0, len(v), 3)]


def find_customer_in_list_of_customers(
    customers_list: list[dict], fname: str, lname: str, pcode: str
) -> bool:
    """
    Проверяет, существует ли клиент с заданными данными в списке клиентов.

    Функция проходит по списку словарей `customers_list` и ищет словарь,
    в котором значения ключей 'First Name', 'Last Name' и 'Post Code'
    соответствуют переданным аргументам.

    Args:
        customers_list (list[dict]): Список клиентов, каждый клиент — словарь с ключами
                                      'First Name', 'Last Name', 'Post Code'
        fname (str): Имя клиента
        lname (str): Фамилия клиента
        pcode (str): Почтовый код клиента

    Returns:
        bool: True, если клиент с указанными данными найден в списке, иначе False.
    """
    for el in customers_list:
        if el["First Name"] == fname:
            if el["Last Name"] == lname and el["Post Code"] == pcode:
                return True
    return False


def if_list_is_sorted_descendingly(lst: list[dict], key: str) -> bool:
    return all(lst[i][key] >= lst[i + 1][key] for i in range(len(lst) - 1))


def get_any_customer_credentials_from_customers(lst: list[dict]):
    return lst[random.randint(0, len(lst) - 1)]


def generate_delete_button_xpath(first_name: str, last_name: str) -> str:
    """
    Генерирует XPath для кнопки Delete в строке таблицы,
    где первый td содержит first_name, а второй td содержит last_name.

    :param first_name: имя клиента
    :param last_name: фамилия клиента
    :return: строка XPath
    """
    xpath = (
        f'//tr[td[1][contains(text(), "{first_name}")] and td[2][contains(text(), "{last_name}")]]'
        '//button[@ng-click="deleteCust(cust)"]'
    )
    return xpath


def get_client_name_to_delete(lst: list[dict]) -> str:
    """
    Получить из таблицы Customers список имен. Узнать длину каждого имени, затем найти среднее
    арифметическое получившихся длин и удалить клиента с тем именем, у которого длина будет ближе
    к среднему арифметическому
    Пример: список имен
    Albus , Neville , Voldemort. Длины имен 5 , 7 , 9 соответственно.
    Среднее арифметическое длин 7 , удаляем имя Neville
    """
    names = [n["First Name"] for n in lst]
    len_names = [len(n) for n in names]
    avg_len = sum(len_names) / len(len_names)
    name = min(names, key=lambda n: abs(len(n) - avg_len))
    last_name, postcode = [(x["Last Name"], x["Post Code"]) for x in lst if x["First Name"] == name][0]
    return name, last_name, postcode
