from tests.conftest import category_1, category_2


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


def test_add_product(category_1, category_2, new_product):
    category_2.add_product(new_product)
    assert category_2.product_count == 4


def test_str_category(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 3 шт."
