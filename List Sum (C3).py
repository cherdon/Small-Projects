def list_sum(values):
    value_list = values
    no_of_values = len(value_list)

    sum = 0.0
    for i in range(no_of_values):
        value = value_list[i]
        sum = sum + value

    return sum

values = [4.25,5.0,10.75]
print(list_sum(values))

values = [5.0]
print(list_sum(values))

values = []
print(list_sum(values))
