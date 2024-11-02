from itertools import product

import pytest

from tests.conftest import category_1, category_2, products_iterator


def test_category(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description == (
        "Смартфоны, как средство не только коммуникации, " "но и получение дополнительных функций для удобства жизни"
    )


def test_category_product_count_1(nullify_category_counters, category_1, category_2):
    assert category_1.category_count == 2
    assert category_1.product_count == 4

    assert category_2.category_count == 2
    assert category_2.product_count == 4


def test_add_product(nullify_category_counters, category_2, new_product):
    category_2.add_product(new_product)
    assert category_2.product_count == 2


def test_str_category(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_iterator(products_iterator):
    iter(products_iterator)
    assert products_iterator.index == 0
    assert next(products_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(products_iterator).name == "Iphone 15"
    assert next(products_iterator).name == "Xiaomi Redmi Note 11"
    with pytest.raises(StopIteration):
        next(products_iterator)


def test_category_add_product_error(category_1):
    with pytest.raises(TypeError):
        category_1.add_product("Product")


def test_category_add_product_smartphone(category_1, product_smartphone1):
    category_1.add_product(product_smartphone1)
    assert category_1.products.split("\n")[-2] == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_middle_price(category_1):
    assert category_1.middle_price() == 140333


def test_middle_price_zero(no_products_category):
    assert no_products_category.middle_price() == 0
