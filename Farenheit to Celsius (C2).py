def farenheit_to_celsius(temp):
    my_temp = temp
    a = 9/5
    b = 32

    return (my_temp - b)/a

temp = float(input("What is your temperature in Kelvins?"))
output = round(farenheit_to_celsius(temp),2)
print(str(output) + "C")