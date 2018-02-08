def is_palindrome(value):
    reverse_value = str(value)[::-1]
    if str(value) == reverse_value:
        result = True
    else:
        result = False
    return result

print(is_palindrome(12321))
print(is_palindrome(12))
print(is_palindrome(1))
print(is_palindrome(22))
print(is_palindrome(123431))