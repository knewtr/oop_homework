from unittest.mock import patch


def test_product(product_test):
    assert product_test.name == "Samsung Galaxy C23 Ultra"
    assert product_test.description == "256GB, Серый цвет, 200MP камера"
    assert product_test.price == 180000.0
    assert product_test.quantity == 5


def test_price_property(product_test):
    assert product_test.price == 180000.0


def test_price_setter_zero(product_test, capsys):
    product_test.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_neg(product_test, capsys):
    product_test.price = -180000.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


# def test_price_setter_change(capsys, product_test):
#     with patch('builtins.input', return_value='y'):
#         product_test.price = 1000.0
#         captured = capsys.readouterr()
#         expected_output = 'Цена ниже изначальной: 180000.0 -> 1000.0. Понизить цену? (y/n)'
#         assert captured.out.strip() == expected_output
#         assert product_test.price == 1000.0


# def test_new_product():
#     new_product = Product.new_product({"name": "Samsung Galaxy C23 Ultra",
#                 "description": "256GB, Серый цвет, 200MP камера",
#                 "price": 180000.0,
#                 "quantity": 5})
#     assert new_product.name == 'Samsung Galaxy C23 Ultra'
#     assert new_product.description == '256GB, Серый цвет, 200MP камера'
#     assert new_product.price == 180000.0
#     assert new_product.quantity == 10
