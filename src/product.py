class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Цена ниже изначальной: {self.__price} -> {value}. Понизить цену? (y/n) ")
            if confirmation == "y":
                self.__price = value
        else:
            self.__price = value

    @classmethod
    def new_product(cls, new_product_dict, products):
        name = new_product_dict["name"]
        description = new_product_dict["description"]
        price = new_product_dict["price"]
        quantity = new_product_dict["quantity"]
        for product in products:
            if product.name == name:
                product.quantity += quantity
                if product.price < price:
                    product.price = price
                return Product(**new_product_dict)
        new_product = cls(name, description, price, quantity)
        products.append(new_product)
        return Product(**new_product_dict)


# if __name__ == '__main__':
#
#     product1 = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = LawnGrass('Grass', 'Nice one', 150, 1, 'Russia', 15, 'grass green')
#     print(product1 + product2)
