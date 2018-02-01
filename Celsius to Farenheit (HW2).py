def celsius_to_farenheit(temp):
    my_temp = temp
    a = 9/5
    b = 32

    return (my_temp * a) + b

temp = float(input("What is your degree in Celsius? \n"))
output = round(celsius_to_farenheit(temp),2)
print(output)
