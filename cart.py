"""
In this class we create methods to add a new product to shopping cart, count total pice in cart
and returns a complete check
"""
import customer
from customer import Customer
from product import Product
class Cart:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity: float = 1):
        if product in self.__products:
            index = self.__products.index(product)
            self.__quantities[index] += quantity
        else:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        return sum(item.price * self.__quantities[index] for index, item in enumerate(self.__products))

    def __str__(self):
        res = '\n'.join(map(
            lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
            zip(self.__products, self.__quantities))
        )

        return f'{customer.Customer}\n{res}\nTotal: {self.total()} UAH'