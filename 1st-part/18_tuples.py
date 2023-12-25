numbers = (1, 2, 3, 4, 5)
strings = ('nico', 'pablo', 'douglas', 'nico')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# You cannot mutate tuples!
# Not allowed
# numbers.append(6)
# numbers[1] = 'change'

print(strings)
print(strings.index('pablo'))
print(strings.index('nico'))


my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'william'
print(my_list)

my_list = tuple(my_list)
print(my_list)
