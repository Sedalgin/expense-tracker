import json


def flow_rate_output (general):
    for x in general:
        print(f"{x['Расходи']} - {x['Сумма']}")


def calculate_total_price(general):
    total_price = 0
    for x in general:
        total_price+=x["Сумма"]
    return total_price

def load_expenses():
    try:
        with open("expenses.json", "r",encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses (exppense_list):
    with open('expenses.json', 'w', encoding="utf-8") as file:
        json.dump(exppense_list,file, ensure_ascii=False, indent=4)

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
    general_list = load_expenses()
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
                print("Надо ввести число!")
                continue
            if value <=0:
                print("Сумма должна біть больше ноля")
                continue

            general_list.append({"Расходи": key, "Сумма": value})
            save_expenses(general_list)
            print(general_list)


        elif user_input == 2:
            flow_rate_output(general_list)


        elif user_input == 3:
            print(f"Ощая сумма расходов составила {calculate_total_price(general_list)} гривен")

        elif user_input == 4:
            filtered_list = []
            check = 0
            for x in general_list:
                if x["Расходи"] not in filtered_list:
                    filtered_list.append(x["Расходи"])
            for x in filtered_list:
                print(f"{filtered_list.index(x)+1} - {x}")
            if not filtered_list:
                print("Расходов пока нет")
                continue
            else:
                try:
                    user_categori = int(input("Виберите категорию из введених Вами продуктов"))
                    if not 1 <= user_categori <= len(filtered_list):
                        print("Ввели не верний номер")
                        continue
                    else:
                        user_categori = filtered_list[user_categori - 1]
                        print(user_categori)
                    for x in general_list:
                        if user_categori == x['Расходи']:
                            check += x['Сумма']
                    print(f"Сумма потраченая на {user_categori} = {check} гривен")
                except ValueError:
                    print("Надо ввести цифру для вибора")

        elif user_input == 5:
            delete_expenses(general_list)

        elif user_input == 6:
            flag = False

        else:
            print("такого пункта НЕТУ !")

main()