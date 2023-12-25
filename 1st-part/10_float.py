x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

# Unofficial workaround
y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))

# Mathematical way
print('*' * 10)

print(y, x)

tolerance = 0.00001
print(abs(x-y) < tolerance)

# My way :D
print(round(y, 2) == x)
