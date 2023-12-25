

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'hi')
print(numbers)

numbers.insert(3, 'change')
print(numbers)


tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

new_list.sort()  # Cannot sort list with different types
