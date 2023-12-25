items = [
    {
        'product': 'Tee Shirt',
        'price': 100,
    },
    {
        'product': 'Pants',
        'price': 300
    },
    {
        'product': 'Cargo',
        'price': 200
    }
]

prices = list(map(lambda item : item['price'], items))
print(prices)

tax = .19

def add_taxes(item):
    item['taxes'] = item['price'] * tax
    return item

# items_with_taxes = list(map(add_taxes, items))

# the Pipe (|) concats the current object with the new one thus not mutating the original one
items_with_taxes = list(map(lambda x : x | {'tax': x['price'] * .19}, items))
print("Items with taxes:      ", items_with_taxes)
print("Items:                 ", items)

# Now using a library
import copy

items_deep_copy = copy.deepcopy(items)
print("Items deep copy:               ", items_deep_copy)
items_copy_with_taxes = list(map(add_taxes, items_deep_copy))
print("Items deep copy with taxes:    ", items_copy_with_taxes)
print("Items deep copy:               ", items_deep_copy)
print("Items:                         ", items)

# another way to avoid mutating the original dict is by copying it
items_shallow_copy = items.copy()
print("Items shallow copy:            ", items_shallow_copy)
items_copy_with_taxes = list(map(add_taxes, items_shallow_copy))
print("Items shallow copy with taxes: ", items_copy_with_taxes)
print("Items shallow copy:            ", items_shallow_copy)
print("Items:                         ", items)

print(id(items))
print(id(items_shallow_copy))
