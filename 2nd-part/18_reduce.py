from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda accumulator, current_value: accumulator + current_value, numbers)

print(result)