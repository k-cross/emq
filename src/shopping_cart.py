'''
[*] This file is for the entire shopping cart and its implementation

[!] This doesn't account for electronic recycling fees 
[!] This doesn't account for product weights
'''


SHIPPING_RATE = 5.50

class ShoppingCart:
    def __init__():
        pass

'''
[*] Calculates the total at checkout

[!] This is just a mockup implementation
'''
def calculateTotal(products, shipping_location):
    # TODO: Add database driver calls to get needed info
    subtotal = 0.0
    total = 0.0
    taxRate = 0.0

    for product in products:
        subtotal += product.price

    total = subtotal + (subtotal * taxRate) + SHIPPING_RATE

    return total
