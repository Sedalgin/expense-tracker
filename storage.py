import json

def load_expenses():
    try:
        with open("expenses.json", "r",encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses (exppense_list):
    with open('expenses.json', 'w', encoding="utf-8") as file:
        json.dump(exppense_list,file, ensure_ascii=False, indent=4)