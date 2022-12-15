"""
In this module we create class Product in which we keep info about products in our shop.
Note that price of product is controlled by raising error if it's lower or equal 0
"""
import exceptions
class Product:

    def __init__(self, title: str, description: str, price: float, weight: float):
        self.title = title
        self.price = price
        if price <= 0:
                raise exceptions.PriceError(self.price, "Price less or equal zero")
        self.weight = weight
        self.description = description

    def __str__(self):
        return f'{self.title}: {self.description}, Volume: {self.weight}, Price: {self.price}'

