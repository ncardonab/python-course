# print(0 / 0)
# print(result)

sum = lambda x, y : x + y + 1
# assert sum(2, 2) == 4 # AssertionError

age = 10
if (age < 18):
    raise Exception("Minors are not allowed")