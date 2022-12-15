import product
import customer
import cart

if __name__ == '__main__':

    beer = product.Product('Beer', 'Chernihivske', 5, 0.5)
    vine = product.Product('Vine', 'Koblevo', 75.00, 0.75)
    samogon = product.Product('Samogon', 'Did Vasyl', 1000.00, 1)

    customer = customer.Customer('Osypenko', 'Kostiantyn', '+380938522850', 'osypenk.k@gmail.com')

    order = cart.Cart(customer)
    order.add_product(beer, 2)
    order.add_product(vine, 1)
    order.add_product(samogon, 1)

    print(order)
