class Category:
    name: str
    description: str
    products: list[dict]
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0


# if __name__ == '__main__':
#     category = Category('Смартфоны', 'Samsung Galaxy C23 Ultra', ['product_1', 'product_2'])
#     print(category.name)
#     print(category.description)
#     print(category.products)
#     print(category.category_count)
#     print(category.product_count)
