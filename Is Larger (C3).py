def is_larger(n1, n2):
    result = "Nothing"

    if n1 > n2:
        result = True
    else:
        result = False
    return result

n1 = float(input("What is the first number? \n"))
n2 = float(input("What is the second number? \n"))
print(is_larger(n1, n2))