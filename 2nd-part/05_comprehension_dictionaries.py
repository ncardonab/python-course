import random
# dict = {}
# for i in range(1, 5):
#     dict[i] = i * 2

# print(dict)

# dict_v2 = { i: i * 2 for i in range(1, 5)}
# print(dict)

countries = ['COL', 'NL', 'AUS', 'FR']
population = {country_name: random.randint(40000, 10000000) for country_name in countries}
print(population)

names = ['nico', 'zule', "santi"]
ages = [12,56,98]

print(list( zip(names, ages) ))

people_ages = {name: age for (name, age) in zip(names, ages)}
print(people_ages)

text = "Hello! I'm Nicolas, and I'm a great engineer"
vocals_ocurrence = {char: text.count(char) for char in text if char in 'aeiou'}
print(vocals_ocurrence)