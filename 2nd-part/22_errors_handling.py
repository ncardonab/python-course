try:
    print(0 / 0)
    assert 1 != 1, 'One is not different than one'
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)

print('The error didn\'t stopped the execution')