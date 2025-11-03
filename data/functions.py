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
    return [dict(zip(k, v[i:i+3])) for i in range(0, len(v), 3)]
    

def find_customer_in_list_of_customers(customers_list, fname, lname, pcode):
    for el in customers_list:
        if el['First Name'] == fname:
            if el['Last Name'] == lname and el['Post Code'] == pcode:
                return True
    return False
