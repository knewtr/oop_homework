class Category:
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
        self.__products.append(product)
        return self.__products

    @classmethod
    def get_full_amount(cls, products):
        for product in products:
            product_amount = 0
            product_amount += product.product_count
            return product_amount


# if __name__ == '__main__':
#     category = Category('Смартфоны', 'Samsung Galaxy C23 Ultra', ['product_1', 'product_2'])
#     # print(category.name)
#     # print(category.description)
#     print(category.products)
#     print(category.category_count)
#     print(category.product_count)
