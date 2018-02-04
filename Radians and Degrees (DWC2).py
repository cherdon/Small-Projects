import math

def rad_to_deg(rad):
    r = rad
    degree = math.degrees(r)

    return degree

def deg_to_rad(deg):
    d = deg
    radians = math.radians(deg)

    return radians

rad = float(input("What is the angle in radians? \n"))
deg = float(input("What is the angle in degrees? \n"))
output1 = round(rad_to_deg(rad),5)
output2 = round(deg_to_rad(deg),5)
print (output1, output2)