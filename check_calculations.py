from calculations import normalize_category
from calculations import calculate_total_price
from calculations import total_by_category

result = normalize_category(" ПРОДУКТИ    ")
result_ = normalize_category(" ")
assert result == 'продукти'
assert result_ == ''
print("Перша перевірка пройдена")


result_01 = calculate_total_price([{'Сумма':200},{'Сумма':200}])
result_01_ = calculate_total_price([])
assert result_01 == 400
assert result_01_ == 0
print("Друга перевірка пройдена")


result_02 = total_by_category([{"Расходи": "Продукти", "Сумма": 200}, {"Расходи":"Продукти", "Сумма": 300}])
result_02_ = total_by_category([])
assert result_02 == {"продукти":500}
assert result_02_ == {}
print("Третя перевірка пройдена")
