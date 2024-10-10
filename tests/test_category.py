from tests.conftest import category_1


def test_category(category_1):
     assert category_1.name == 'Смартфоны'
     assert category_1.description == ('Смартфоны, как средство не только коммуникации, '
                                       'но и получение дополнительных функций для удобства жизни')
     assert category_1.products == [
             {
                 "name": "Samsung Galaxy C23 Ultra",
                 "description": "256GB, Серый цвет, 200MP камера",
                 "price": 180000.0,
                 "quantity": 5
             },
             {
                 "name": "Iphone 15",
                 "description": "512GB, Gray space",
                 "price": 210000.0,
                 "quantity": 8
             },
             {
                 "name": "Xiaomi Redmi Note 11",
                 "description": "1024GB, Синий",
                 "price": 31000.0,
                 "quantity": 14
             }
        ]


def test_category_product_count(category_1, category_2):
    assert category_1.category_count == 2
    assert category_2.product_count == 4
