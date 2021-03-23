def power(base, exp=4):
    if all([type(x) != int for x in (base, exp)]):
        raise TypeError("Both arguments should be integer")
    else:
        return base**exp


print(power(2, 3))