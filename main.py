import json
from calculations import calculate_total_price
from calculations import total_by_category
from storage import load_expenses
from storage import save_expenses
from expense import Expense

def flow_rate_output (general):
    for x in general:
        print(f"{x['Расходи']} - {x['Сумма']}")

def list_output(expense_list):
    for y,item in enumerate(expense_list):
        print(f"{y+1} - {item['Расходи']} - {item['Сумма']} грн")

def delete_expenses (expense_list):
    list_output(expense_list)
    try:
        user_input = int(input("Введите число для удаление пункта растрат "))
        if 1<=user_input <= len(expense_list):
            product_removed = expense_list[user_input-1]
            del expense_list[user_input - 1]
            print(f"Категория - {product_removed['Расходи']} - УСПЕШНО УДАЛЕНА")
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
        print("Обнаружено что файл проврежден ! ")
        return

    while flag:

        print("Добавить расход — 1")
        print("Вывести расходы — 2")
        print("Общая сумма — 3")
        print("Виберите категорию растрат - 4")
        print("Удаление расхода - 5")
        print("Выход — 6")

        try:
            user_input = int(input("Сделайте свой выбор: "))
        except ValueError:
            print("Надо ввести число")
            continue

        if user_input == 1:

            key = input("Название расходов: ")
            try:
                value = int(input("Потраченая сумма: "))
            except ValueError:
                print("Надо ввести число")
            else:
                try:
                    cost_object = Expense(key, value)
                except ValueError as e:
                    print(e)
                else:
                    general_list.append(cost_object.to_dict())
                    save_expenses(general_list)

        elif user_input == 2:
            flow_rate_output(general_list)
            print("Всего расходи по категоріям")
            for x,y in total_by_category(general_list).items():
                print(f"{x} - {y} грн")


        elif user_input == 3:
            print(f"Ощая сумма расходов составила {calculate_total_price(general_list)} грн. ")

        elif user_input == 4:
            all_squandered =[]
            total_dict = total_by_category(general_list)
            for y,x in enumerate(total_dict,start=1):
                all_squandered.append(x)
                print(f"{y} - {x}")

            if not all_squandered:
                print("Расходов пока нет")
                continue
            else:
                try:
                    user_category = int(input("Виберите категорию из введених Вами продуктов: "))
                    if not 1 <= user_category <= len(all_squandered):
                        print("Ввели не верний номер")
                        continue
                    else:
                        user_category = all_squandered[user_category - 1]
                        print(f"Сумма потраченая на {user_category} = {total_dict[user_category]} гривен")
                except ValueError:
                    print("Надо ввести цифру для вибора")

        elif user_input == 5:
            delete_expenses(general_list)

        elif user_input == 6:
            flag = False

        else:
            print("такого пункта НЕТУ !")

if __name__ == "__main__":
    main()