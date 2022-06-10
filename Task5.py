from functools import reduce
print(reduce((lambda multiplied, multiplier: multiplied * multiplier), [el for el in range(100, 1001) if el % 2 == 0]))
