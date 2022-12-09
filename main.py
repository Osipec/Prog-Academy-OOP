class Product:

    def __init__(self, title: str, description: str, price: float, weight: float):
        self.title = title
        self.price = price
        self.weight = weight
        self.description = description

    def __str__(self):
        return f'{self.title}: {self.description}, Volume: {self.weight}, Price: {self.price}'


class Customer:

    def __init__(self, surname: str, name: str, phone: str, email: str):
        self.surname = surname
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.surname} {self.name}; {self.phone}, {self.email}'


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

        return f'{customer}\n{res}\nTotal: {self.total()} UAH'


beer = Product('Beer', 'Chernihivske', 32.00, 0.5)
vine = Product('Vine', 'Koblevo', 75.00, 0.75)
samogon = Product('Samogon', 'Did Vasyl', 1000.00, 1)

customer = Customer('Osypenko', 'Kostiantyn', '+380938522850', 'osypenk.k@gmail.com')

order = Cart(customer)
order.add_product(beer, 2)
order.add_product(vine, 1)
order.add_product(samogon, 1)

print(order)
