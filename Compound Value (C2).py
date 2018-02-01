def compound_value (amt, rate):
    a = rate
    interest = 1 + (amt/12)
    b = a*((interest * (1 - interest ** 6))/(1 - interest))
    c = round (b,2)
    return c

c = float(input("What is your monthly saving rate?"))
b = float(input("What is your annual interest rate?" ))

compounded = compound_value (b,c)
print("After the sixth month, the account value is " + str(compounded))

