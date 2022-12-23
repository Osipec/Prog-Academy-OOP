import product
import customer
import cart

if __name__ == '__main__':

    beer = product.Product('Beer', 'Chernihivske', 5, 0.5)
    vine = product.Product('Vine', 'Koblevo', 75.00, 0.75)
    samogon = product.Product('Samogon', 'Did Vasyl', 1000.00, 1)
    juice = product.Product('Juice', 'Jaffa', 50, 1)

    customer = customer.Customer('Osypenko', 'Kostiantyn', '+380938522850', 'osypenk.k@gmail.com')

    order = cart.Cart(customer)
    order.add_product(beer, 2)
    order.add_product(vine, 2)
    order.add_product(samogon, 1)
    order.add_product(juice, 4)

    print(f'{order}\n')

    for item, quantity in order:
        print(item, quantity, item.price*quantity)
    print()

    print(f'Get item:\n{order[0]}')
    for item in order[0:2]:
        print(f'Sliced: {item}')
    print(f'Get slice:\n{order[0:2]}')
