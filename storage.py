import json

def load_expenses(file_path="expenses.json"):
    try:
        with open(file_path, "r",encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses (expense_list, file_path="expenses.json"):
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(expense_list,file, ensure_ascii=False, indent=4)