import pytest
from expense import Expense


def test_expense_creation():
    test_1 = Expense("test", 100)
    assert test_1.amount == 100
    assert test_1.category == "test"


def test_string_repr():
    test_1 = Expense("test", 100)
    assert str(test_1) == "test = 100 грн"
    assert repr(test_1) == "Expense('test', 100)"


def test_change_amount():
    test_1 = Expense("test", 100)
    test_1.change_amount(250)
    assert test_1.amount == 250


@pytest.mark.parametrize("new_amount", [-20, 0])
def test_change_new_amount(new_amount):
    test_1 = Expense("test", 100)
    with pytest.raises(ValueError):
        test_1.change_amount(new_amount)
    assert test_1.amount == 100


@pytest.mark.parametrize("new_amount", [-20, 0])
def test_1_expense_creation(new_amount):
    with pytest.raises(ValueError):
        test_1 = Expense("test", new_amount)


@pytest.mark.parametrize("amount, expected",
                         [
                             (200, False),
                             (150, False),
                             (100, True),
                             (50, True),
                         ])
def test_is_large(amount, expected):
    test_1 = Expense("test", 100)
    a = test_1.is_large(amount)
    assert a == expected


@pytest.mark.parametrize("expense, expected",
                         [
                            (Expense("Такси", 150),
                             {"Категория": "Такси", "Сумма": 150}),
                         ])
def test_to_dict(expense, expected):
    x = expense.to_dict()
    assert x == expected


def test_to_dict_change_amount():
    test = Expense("Такси", 150)
    test.change_amount(100)
    x = test.to_dict()
    assert x["Сумма"] == 100
