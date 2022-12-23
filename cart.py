"""
In this class we create methods to add a new product to shopping cart, count total pice in cart
and returns a complete check
"""
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

        return f'{self.customer}\n{res}\nTotal: {self.total()} UAH'

    def __iter__(self):
        return CartIter(self.__products, self.__quantities)

    def __getitem__(self, item):
        if isinstance(item, int):
            if item > len(self.__products):
                raise IndexError
            return self.__products[item]
        if isinstance(item, slice):
            res = []
            start = item.start or 0
            stop = item.stop or len(self.__products)
            step = item.step or 1

            for i in range(start, stop, step):
                res.append(self.__products[i])
            return res

        raise TypeError()

    def __len__(self):
        return len(self.__products)


class CartIter:

    def __init__(self, products: list, quantities: list):
        self.products = products
        self.quantities = quantities
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1], self.quantities[self.index - 1]
        raise StopIteration
