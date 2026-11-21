LIST_OF_CATEGORIES_TO_CHOOSE_FROM = ["Продукты", "Жилье", "Транспорт", "Здоровье", "Шопинг"]


def normalize_category(text):
    text = text.strip().lower()
    return text


def category_by_number(number):
    if number > len(LIST_OF_CATEGORIES_TO_CHOOSE_FROM):
        raise ValueError("Значение больше")
    elif number <= 0:
        raise ValueError("Значение меньше или равно 0")
    else:
        return LIST_OF_CATEGORIES_TO_CHOOSE_FROM[number-1]


def calculate_total_price(general):
    total_price = 0
    for spending in general:
        total_price += spending["Сумма"]
    return total_price


def total_by_category(expense_list):
    product_dictionary = {}
    if len(expense_list) > 0:
        for spending in expense_list:
            product = spending['Категория']
            product_dictionary[normalize_category(product)] = 0

        for spending in expense_list:
            items = normalize_category(spending['Категория'])
            summa_items = spending["Сумма"]
            if items in product_dictionary:
                product_dictionary[items] += summa_items

        return product_dictionary
    else:
        return {}


def filter_by_min_amount(expense_list, min_amount):
    filter_list = []
    for spending in expense_list:
        if spending["Сумма"] >= min_amount:
            filter_list.append(spending)
    return filter_list
