numbers = []

for element in range(1, 11):
    numbers.append(element)

print(numbers)
print([element for element in range(1, 11)])

is_even = lambda x : x % 2 == 0
even_numbers_squared = [number ** 2 for number in numbers if is_even(number)]
print(even_numbers_squared)
