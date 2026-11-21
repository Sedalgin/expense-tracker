import pytest
import json
from calculations import normalize_category
from calculations import calculate_total_price
from calculations import total_by_category
from storage import load_expenses
from storage import save_expenses
from calculations import filter_by_min_amount
from calculations import category_by_number
from calculations import LIST_OF_CATEGORIES_TO_CHOOSE_FROM


@pytest.mark.parametrize("number", [0, -1, 6])
def test_category_by_number(number):
    with pytest.raises(ValueError):
        category_by_number(number)


@pytest.mark.parametrize("number", [1, 2, 5])
def test_category_by_number_1(number):
    result = category_by_number(number)
    assert result == LIST_OF_CATEGORIES_TO_CHOOSE_FROM[number-1]


@pytest.mark.parametrize(
    "text,expected",
    [
        ("ЕДА", "еда"),
        (" еда ", "еда"),
        ("ЕдА", "еда"),
        ("", ""),
        (" ", "")
    ]
)
def test_normalize_category(text, expected):
    assert normalize_category(text) == expected


@pytest.mark.parametrize(
    "expense_list, min_amount, expected",
    [
        ([{"Категория": "Продукти", "Сумма": 200}], 2,
         [{"Категория": "Продукти", "Сумма": 200}]),
        ([], 200, []),
        ([{"Категория": "Продукти", "Сумма": 200}], 400, []),
        ([{"Категория": "Продукти", "Сумма": 200}, {"Категория": "Продукти", "Сумма": 200},
          {"Категория": "Машина", "Сумма": 400}], 200,
         [{"Категория": "Продукти", "Сумма": 200}, {"Категория": "Продукти", "Сумма": 200},
          {"Категория": "Машина", "Сумма": 400}])
    ]
)
def test_filter_by_min_amount(expense_list, min_amount, expected):
    assert filter_by_min_amount(expense_list, min_amount) == expected


def test_calculate_total_price():
    result = calculate_total_price([{"Категория": "Продукти", "Сумма": 300},
                                    {"Категория": "Продукти", "Сумма": 300, }])
    assert result == 600


def test_total_by_category():
    result = total_by_category([{"Категория": "Продукти", "Сумма": 300},
                                {"Категория": "Продукти", "Сумма": 300, }])
    assert result == {"продукти": 600}


def test_save_expenses(tmp_path):
    file_path = tmp_path / "expenses.json"
    test_list = [{"Категория": "Продукти", "Сумма": 300},
                 {"Категория": "Продукти", "Сумма": 300, }]
    save_expenses(test_list, file_path)
    result_1 = load_expenses(file_path)
    assert result_1 == test_list


def test_normalize_category_1():
    result = normalize_category(" ")
    assert result == ""


def test_calculate_total_price_1():
    result = calculate_total_price([])
    assert result == 0


def test_total_by_category_1():
    result = total_by_category([])
    assert result == {}


def test_load_file(tmp_path):
    test = tmp_path / "missing.json"
    load_test = load_expenses(test)
    assert load_test == []
    assert not test.exists()


def test_invalid_number():
    with pytest.raises(ValueError):
        int("Hello world")


def test_load_invalid_json(tmp_path):
    test = tmp_path / "broken.json"
    test.write_text("{broken", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_expenses(test)
