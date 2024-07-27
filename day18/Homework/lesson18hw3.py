shop_products = {}
o = None
oo = 'product_n'
ooo = 0

while o != 'x':
    ooo = ooo + 1
    ooo = str(ooo)
    oo = oo + ooo
    o = input('Please enter either a name of a desired product or x: ')
    if o != 'x':
        shop_products.update({oo : o})
    ooo = int(ooo)
    oo = 'product_n'

print(shop_products.values())
    
    