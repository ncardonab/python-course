numbers = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8]
numbers_3 = [6, 7, 8]

times_2 = list(map(lambda number : number * 2, numbers))
print(times_2)

sum_of_arrays = list( map(lambda x, y: x + y, numbers, numbers_2) )
print('Sum of arrays', sum_of_arrays)

sum_of_arrays_2 = list( map(lambda x, y, z: x + y + z, numbers, numbers_2, numbers_3) )
print('Sum of arrays', sum_of_arrays_2)