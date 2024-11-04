from src.base_order import BaseOrder
from src.product import Product


class Category(BaseOrder):
    name: str
    description: str
    products: list[dict]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        total_prod_amount = 0
        for product in self.product_list:
            total_prod_amount += product.quantity
        return f"{self.name}, количество продуктов: {total_prod_amount} шт."

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def product_list(self):
        return self.__products

    def add_product(self, product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def get_order_info(self):
        return f"Наименование: {Product.name}, Количество: {Product.quantity}, Цена: {Product.price}"

    def middle_price(self):
        if not self.__products:
            return 0
        else:
            return round(sum([product.price for product in self.__products]) / len(self.__products))
