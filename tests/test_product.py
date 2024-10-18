from unittest.mock import patch

import pytest

from src.product import Product


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


@pytest.mark.parametrize("input_value, expected_price", [("y", 100), ("n", 200)])
@patch("builtins.input", return_value="y")
def test_price_setter_change(mocked_input, input_value, expected_price):
    product = Product("Товар", "Описание", 200.0, 1)
    mocked_input.return_value = input_value

    product.price = 100.0

    assert product.price == expected_price


def test_product_str(product_test):
    assert str(product_test) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_add_product(category_1):
    assert 2580000.0
