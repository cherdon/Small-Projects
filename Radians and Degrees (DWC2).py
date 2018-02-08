import math

def rad_to_deg(rad):
    r = rad
    degree = round(math.degrees(r),5)

    return degree

def deg_to_rad(deg):
    d = deg
    radians = round(math.radians(deg),5)

    return radians

rad = float(input("What is the angle in radians? \n"))
deg = float(input("What is the angle in degrees? \n"))
output1 = rad_to_deg(rad)
output2 = deg_to_rad(deg)
print (output1, output2)