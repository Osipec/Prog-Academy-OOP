"""
This exception is called if the price of product is less or equal 0
"""
class PriceError(Exception):
    def __init__(self, value: float, message: str):
        self.value = value
        self.message = message

    def __str__(self):
        return f'{self.value}, {self.message}'
