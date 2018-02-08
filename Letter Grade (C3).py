def letter_grade(no):

    if no not in range(101):
        result = None
    elif no >= 90:
        result = "A"
    elif no >= 80:
        result = "B"
    elif no >= 70:
        result = "C"
    elif no >= 60:
        result = "D"
    else:
        result = "E"
    return result


no = float(input("What is your score? \n"))
print(letter_grade(no))
