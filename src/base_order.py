from abc import ABC, abstractmethod


class BaseOrder(ABC):

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    @classmethod
    @abstractmethod
    def get_order_info(cls, *args, **kwargs):
        pass
