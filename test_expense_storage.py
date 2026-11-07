from practice_oop import Expense
from storage import save_expenses
from storage import load_expenses


def test_save_expenses(tmp_path):
    test_list = []
    test_1 = Expense("Такси",150)
    test_text = tmp_path / "test_save_expenses.json"
    x = test_1.to_dict()
    test_list.append(x)
    save_expenses(test_list,test_text)
    y = load_expenses(test_text)
    assert test_list == y

    test_2 = Expense(y[0]["Расходи"],y[0]["Сумма"])

    assert test_1.category == test_2.category
    assert test_1.amount == test_2.amount

    test_2.change_amount(200)

    assert test_2.amount == 200
    assert test_1.amount == 150

    test_list_1 = []
    test_text_1 = tmp_path / "test_save_expenses_1.json"
    x = test_2.to_dict()
    test_list_1.append(x)
    save_expenses(test_list_1,test_text_1)
    y_1 = load_expenses(test_text_1)
    test_3 = Expense(y_1[0]["Расходи"],y_1[0]["Сумма"])
    assert test_list_1 == y_1
    assert test_3.amount == 200