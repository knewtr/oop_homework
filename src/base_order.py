from abc import ABC, abstractmethod


class BaseOrder(ABC):

    @classmethod
    @abstractmethod
    def get_order_info(cls, *args, **kwargs):
        pass
