def divisor_set(n: int):
    divisors = {1}
    for i in range(2, n+1):
        if n % i == 0:
            divisors.add(i)

    return divisors

def greatest_common_divisor(n):
    result_list = []
    for each in n:
        result_list.append(divisor_set(each))

    common_divisors = result_list[0]
    for each in result_list:
        common_divisors &= each
       
    return max(common_divisors)

print(greatest_common_divisor([15, 70, 10, 5]))


def greatest_divisor(n: int):
    for i in range(1, n):
        if n % i == 0:
            divisor = i
    return divisor         

def greatest_disisors(n: list):
    divisor_list = []
    for each in n:
        divisor_list.append(greatest_divisor(each))

    return divisor_list

print(greatest_disisors([4, 9, 11]))