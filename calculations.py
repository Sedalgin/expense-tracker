def normalize_category(text):
    text = text.strip().lower()
    return text

def calculate_total_price(general):
    total_price = 0
    for x in general:
        total_price+=x["Сумма"]
    return total_price

def total_by_category(expense_list):
    product_dictionary = {}
    if len(expense_list)>0:
        for x in expense_list:
            product = x['Расходи']
            product_dictionary[normalize_category(product)] = 0

        for y in expense_list:
            items = normalize_category(y['Расходи'])
            summa_items = y["Сумма"]
            if items in product_dictionary:
                product_dictionary[items] += summa_items

        return product_dictionary
    else:
        return {}


def filter_by_min_amount(expense_list, min_amount):
    filter_list = []
    for x in expense_list:
        if x["Сумма"] >= min_amount:
            filter_list.append(x)
    return filter_list
