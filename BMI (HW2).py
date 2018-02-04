def bmi(height, weight):
    h = height * 0.0254
    w = weight * 0.45359237
    result = w / (h ** 2)

    return result

weight = float(input("What is your weight in pounds? \n"))
height = float(input("What is your height in inches? \n"))
output = round(bmi(height, weight),4)
print (output)