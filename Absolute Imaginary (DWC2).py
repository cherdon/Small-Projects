import numpy as np

def absolute(z):
    x = z.real
    y = z.imag
    value = ((x ** 2) + (y ** 2)) ** 0.5
    return value


z = input("What is the complex number? \n")
print(absolute(z))
