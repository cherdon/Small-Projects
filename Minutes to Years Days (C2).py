def minutes_to_years_days(m):
    my_m = m
    d = 1440
    y = 365

    return int((my_m/d)/y),(float((my_m/d)/y)-int((my_m/d)/y))*y

m = float(input("How many minutes?"))
output = minutes_to_years_days(m)
years,days = minutes_to_years_days(m)
print(str(m) + " minutes is " + str(years) + " years and " + str(days) + " days!")