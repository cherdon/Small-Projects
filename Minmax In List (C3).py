import sys

def minmax_in_list(values):
    value_list = values
    no_of_values = len(value_list)
    if no_of_values == 0:
        return None, None
    else:
        minimum = values[0]
        maximum = values[0]
        for i in values:
            if i < minimum:
                minimum = i
            elif i > maximum:
                maximum = i
            else:
                minimum = minimum
                maximum = maximum
        return (minimum, maximum)



values = [1,2,3,4,5]
print(minmax_in_list(values))

values = [1]
print(minmax_in_list(values))

values = []
print(minmax_in_list(values))

values = [1,1,1,1,1]
print(minmax_in_list(values))

values = [0, 10]
print(minmax_in_list(values))

values = [10, 4, 9, 0]
print(minmax_in_list(values))