def area_vol_cylinder(r, l):
    radius = r
    length = l
    area = radius * radius * float(pi)
    volume = area * length

    return volume

radius = float(input("What is the radius? \n"))
length = float(input("What is the length of the cylinder? \n"))
output = area_vol_cylinder(r, l)
print(output)