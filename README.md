# Expense Tracker

A console program that keeps a list of your expenses.

## Features
- Add new expenses
- Show all saved expenses
- Show the total amount spent
- Show how much was spent on a selected category
- Delete expenses you no longer need

## Technologies
- Python 3.14.5
- Input data is validated with `@property`; other functions also use `try/except`
- 32 tests (pytest)
- Magic methods `__repr__` and `__str__`
- Data is stored in a JSON file

## Example
The program interface is in Russian.

```
> python main.py
Добавить расход — 1
Вывести расходы — 2
Общая сумма — 3
Виберите категорию растрат - 4
Удаление расхода - 5
Выход — 6
Сделайте свой выбор: 2
Продукти  - 200
Всего расходи по категоріям
продукти - 200 грн
```

## How to run
For Windows (cmd):

```
git clone https://github.com/Sedalgin/expense-tracker.git
cd expense-tracker
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py
```

## Tests
The tests are already written. If something in the code breaks, they show where.

```
python -m pytest
```

Expected result: `32 passed`

Tests use pytest 9.1.1.

## Project structure
- `main.py` — the main program (menu); run it to start the tracker
- `storage.py` — reads and writes data to the JSON file
- `calculations.py` — calculations and bringing category names to one format
- `expense.py` — the `Expense` class; `@property` does not allow an amount <= 0
- `requirements.txt` — the libraries the project needs
- `pytest.ini` — pytest settings
- `tests/test_calculations.py` — tests
- `tests/test_expense.py` — tests
- `tests/test_expense_storage.py` — tests

## What I learned
- Splitting the code into modules for readability: (1) saving and reading the file, (2) calculations, (3) validating and working with the object's value, (4) the main file, (5) tests
- Writing a class (`Expense`) with `@property` and magic methods, and importing it into the main file
- Writing tests with pytest, including the `@pytest.mark.parametrize` decorator
- `@property`: the setter validates the value every time it changes; I also understood the role of the getter
- Working with the terminal and its basic commands
- Creating a repository and commits, using `.gitignore`
- Writing Markdown
- Working with dictionaries and lists
- Using `if __name__ == "__main__"`: the code inside runs only in the file that was started directly. It does not block importing, but the code under it does not run in the importing file
- Reading and writing JSON files
- Using `try/except/else`
- Creating a virtual environment (`venv`)
- Listing the required libraries in a text file (`requirements.txt`) and installing them with `pip install -r`
