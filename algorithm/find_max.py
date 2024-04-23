# between 3 values
def find_max_value(a, b, c,):
    max_value = a if a > b else b
    if max_value == b:
        max_value = c if c > b else b

    return max_value


print(find_max_value(5, 4, 3))

# between n values
def find_max_value_n(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num

    return max_value

print(find_max_value_n([1, 5, 18, 9, 1, 12])) 

