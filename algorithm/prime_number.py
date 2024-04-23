def check_prime_number(numbers):
    for num in numbers:
        result = True
        for i in range(2, num):
            if num % i == 0:
                result = False
                print(f"{num}: False")
                break
        if result:    
            print(f"{num}: True")

check_prime_number([1, 2, 3, 4, 5, 6, 7, 8, 9])


# def prime_num(num):
#     for div_num in range(2, num):
#         if num % div_num == 0:
#             return False
#     return True

# for item in [2]:
#     print(f"{item}: {prime_num(item)}")

