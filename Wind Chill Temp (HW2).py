def wind_chill_temp(to, v):
    outside_temp = to
    velocity = v
    twc = 35.74 + 0.6215 * outside_temp - ((35.75) * ((velocity)**0.16)) + 0.4275 * (outside_temp) * ((velocity)**0.16)
    return twc

to = float(input("What is the outside temperature? \n"))
v = float(input("What is the speed in miles per hour? \n"))
output = round(wind_chill_temp(to, v),5)
print (output)