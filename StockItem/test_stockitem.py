import pytest
from StockItem import StockItem

@pytest.mark.parametrize("number", [-1, -2, -3, -4, -5])

def test_stock_item(number):
    with pytest.raises(ValueError):
        x = StockItem("test",number)

def test_sell_amount():
    x = StockItem("test_1", 2)
    with pytest.raises(ValueError):
        x.sell(-1)

@pytest.mark.parametrize("object_1,amount,expected", [
    (StockItem("test_1",2),1,1),
    (StockItem("test_2",2),2,0),
    (StockItem("test_3",10),7,3),
])

def test_sell(object_1,amount,expected):
    x = object_1
    x.sell(amount)
    assert x.quantity == expected

@pytest.mark.parametrize("number", [3,4,5,6])

def test_sell_1(number):
    x = StockItem("test_1", 2)
    with pytest.raises(ValueError):
        x.sell(number)

def test_object():
    x = StockItem("test",1)
    y = StockItem("test",1)
    assert x == y