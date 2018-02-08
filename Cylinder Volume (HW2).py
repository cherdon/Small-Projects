import math

def area_vol_cylinder(r, l):
    radius = r
    length = l
    area = radius * radius * math.pi
    volume = area * length

    return area, volume

r = float(input("What is the radius? \n"))
l = float(input("What is the length of the cylinder? \n"))
output = area_vol_cylinder(r, l)
a, v = area_vol_cylinder(r, l)
print(round(a,2), round(v,2))