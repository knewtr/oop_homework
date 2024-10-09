class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == '__main__':
#     product = Product('Samsung A23', 'Новый телефон', 25000.00, 1)
#     print(product)
