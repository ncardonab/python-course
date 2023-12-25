my_iter = iter(range(1, 11))
print(my_iter)
print(my_iter.__next__())
print(next( my_iter ))
print(my_iter.__next__())

fruit_name = 'Melon'
fruit_iter = iter(fruit_name)
print(fruit_iter)
print(next( fruit_iter ))
print(next( fruit_iter ))
print(next( fruit_iter ))
print(next( fruit_iter ))
print(next( fruit_iter ))
# print(next( fruit_iter )) # Throws StopIteration Error

# Something interesting is that a for is just pure syntactic sugar
groceries = ['butter', 'salt', 'meat', 'oat', 'milk', 'strawberries'] # contains an __iter__() method so it's an iterable
groceries_iter = iter(groceries)

# This is the same as:
while True:
    try:
        next_grocery = next(groceries_iter) 
        print(next_grocery)
    except StopIteration:
        break

# This
for grocery in groceries:
    print(grocery)