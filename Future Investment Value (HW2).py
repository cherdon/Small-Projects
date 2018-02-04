def investment_val(amt, percent, years):
    cash = amt
    ir = percent/1200
    no = years
    mths = no * 12
    result = cash * ((1 + ir )** mths)
    value = round(result,2)

    return value

amt = float(input("What is your investment amount? \n"))
percent = float(input("What is your annual interest rate? \n"))
years = float(input("How many years are you investing in? \n"))
output = investment_val(amt, percent, years)
print(output)
