def sum(x, y):
    return x + y

def hof(x, y, func):
    return ( x + y ) * func(x, y)

print(hof(2, 3, sum))