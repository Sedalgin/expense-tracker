import json
from calculations import calculate_total_price
from calculations import total_by_category
from calculations import category_by_number
from calculations import LIST_OF_CATEGORIES_TO_CHOOSE_FROM
from storage import load_expenses
from storage import save_expenses
from expense import Expense


def list_output(expense_list):
    for number, item in enumerate(expense_list):
        print(f"{number+1} - {item['Категория']} - {item['Сумма']} грн.")


def delete_expenses(expense_list):
    list_output(expense_list)
    try:
        user_input = int(input("Введите число для удаления пункта растрат: "))
        if 1 <= user_input <= len(expense_list):
            product_removed = expense_list[user_input-1]
            del expense_list[user_input - 1]
            print(f"Категория - {product_removed['Категория']} - УСПЕШНО УДАЛЕНА✅")
            save_expenses(expense_list)
        else:
            print("Надо ввести число предлагаемое из списка")
    except IndexError:
        print("Список ПУСТ")
    except ValueError:
        print("Нужно ввести ЧИСЛО")


def main():
    flag = True
    try:
        general_list = load_expenses()
    except json.JSONDecodeError:
        print("Обнаружено что файл поврежден ! ")
        return

    while flag:

        print("Добавить расход — 1")
        print("Вывести расходы — 2")
        print("Общая сумма — 3")
        print("Выберите категорию растрат - 4")
        print("Удаление расхода - 5")
        print("Выход — 6")

        try:
            user_input = int(input("Сделайте свой выбор: "))
        except ValueError:
            print("Надо ввести число!")
            continue

        if user_input == 1:
            for number, category in enumerate(LIST_OF_CATEGORIES_TO_CHOOSE_FROM, start=1):
                print(f"{number} - {category}")
            try:
                category_number = int(input("Выберите категорию растрат с списка: "))
            except ValueError:
                print("Надо ввести число!")
                continue
            try:
                category_from_list = category_by_number(category_number)
            except ValueError as e:
                print(e)
                continue
            try:
                summ = int(input("Потраченная сумма: "))
            except ValueError:
                print("Надо ввести число!")
                continue
            try:
                cost_object = Expense(category_from_list, summ)
            except ValueError as e:
                print(e)
                continue
            general_list.append(cost_object.to_dict())
            save_expenses(general_list)

        elif user_input == 2:
            print("Всего расходов по категориям")
            for category, summ in total_by_category(general_list).items():
                print(f"{category} - {summ} грн")

        elif user_input == 3:
            print(f"Общая сумма расходов составила {calculate_total_price(general_list)} грн. ")

        elif user_input == 4:
            all_squandered = []
            total_dict = total_by_category(general_list)

            for number, category in enumerate(total_dict, start=1):
                all_squandered.append(category)
                print(f"{number} - {category}")

            if not all_squandered:
                print("Расходов пока нет")
                continue
            else:
                try:
                    user_category = int(input(
                        "Выберите категорию продукта чтоб увидеть потраченную сумму: "))
                    if not 1 <= user_category <= len(all_squandered):
                        print("Ввели не верный номер!")
                        continue
                    else:
                        user_category = all_squandered[user_category - 1]
                        print(f"Сумма потраченная на "
                              f"{user_category} = {total_dict[user_category]} грн.")
                except ValueError:
                    print("Надо ввести цифру для выбора!")

        elif user_input == 5:
            delete_expenses(general_list)

        elif user_input == 6:
            flag = False
            print("Програма завершила работу")

        else:
            print("Такого пункта НЕТУ !")


if __name__ == "__main__":
    main()
