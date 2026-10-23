import pytest
import json
from calculations import normalize_category
from calculations import calculate_total_price
from calculations import total_by_category
from storage import load_expenses
from storage import save_expenses

def test_normalize_category():
    result = normalize_category(" ПРОДУКТИ ")
    assert result == "продукти"

def test_calculate_total_price():
    result = calculate_total_price([{"Расходи": "Продукти", "Сумма": 300}, {"Расходи": "Продукти", "Сумма": 300, }])
    assert result == 600

def test_total_by_category():
    result = total_by_category([{"Расходи": "Продукти", "Сумма": 300}, {"Расходи": "Продукти", "Сумма": 300, }])
    assert result == {"продукти": 600}

def test_save_expenses(tmp_path):
    file_path = tmp_path / "expenses.json"
    test_list = [{"Расходи": "Продукти", "Сумма": 300}, {"Расходи": "Продукти", "Сумма": 300, }]
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