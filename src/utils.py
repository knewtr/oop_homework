import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data


def create_objs_from_json(data):
    categories = []
    for category in data:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories.append(Category(**category))

    return categories


# if __name__ == '__main__':
#     raw_data = read_json('../data/products.json')
#     data = create_objs_from_json(raw_data)
#     print(data[0].name)
#     print(data[1].name)
