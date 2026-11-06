import pytest
from practice_producte import Product
from practice_producte import calculate_product_total

@pytest.mark.parametrize("test_input",[-1,-20,-60])

def test_product(test_input):
    with pytest.raises(ValueError):
        test = Product("test",test_input)

def test_product_string():
    test = Product("test",100)
    with pytest.raises(ValueError):
        test.change_price(-10)
    assert test.price == 100

def test_price():
    test = Product("test",0)
    assert test.price == 0

@pytest.mark.parametrize("test_input, expected",
    [
        ([],0),
        ([Product("test",0),Product("test",20),
          Product("twins",30) ],50),
        ([Product("test",100), Product("test",100)],200)
    ]
)

def test_calculate_product_total(test_input, expected):
    x = calculate_product_total(test_input)
    assert x == expected