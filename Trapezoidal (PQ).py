import numpy as np

def trapezoidal(a,b):
    sina = np.sin(a)
    sinb = np.sin(b)
    integrate = (b - a)* ((sinb + sina)/2)
    result = round(integrate,2)

    return result

print(trapezoidal(6,5))
print(trapezoidal(5,5))
print(trapezoidal(2,5))
print(trapezoidal(3,2))