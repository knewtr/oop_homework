from src.base_order import BaseOrder
from src.product import Product


class Order(Product, BaseOrder):

    def __init__(self, product, quantity, total_price):
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        return self.quantity * self.product.price

    def get_order_info(self):
        return f"Наименование: {self.product.name}, Количество: {self.quantity}, Общая стоимость: {self.total_price} "


# if __name__ == '__main__':
#
#     product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     order = Order(product, 1, 180000.0)
#
#     print(order.get_order_info())
