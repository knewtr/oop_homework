import pytest


def test_product_smartphone(product_smartphone1):
    assert product_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_smartphone_sum(product_smartphone1, product_smartphone2):
    assert product_smartphone1 + product_smartphone2 == 2580000.0


def test_smartphone_sum_error(product_smartphone1, product_smartphone2):
    with pytest.raises(TypeError):
        result = product_smartphone1 + 1
