def get_divizors(n):
    result = [1]

    for each in range(2, n):
        if n % each == 0:
            result.append(each)
    return result

print(get_divizors(6))

def perfect_num(n):
    return n == sum(get_divizors(n))

print(perfect_num(496))


from functools import reduce 
from operator import mul
import copy


def factorize_helper(n, result, start=2):  
    mul_list = copy.copy(result)
    mul_list.append(start)        
    mul_result = reduce(mul, mul_list)

    if  mul_result == n:
            return mul_list

    if mul_result < n:
        return factorize_helper(n, result=mul_list)

    elif mul_result > n:
        mul_list.pop(-1)
        start = mul_list.pop(-1) + 1
        return factorize_helper(n, result=mul_list, start=start)
            

def factorize(n):
    result = []
    for each in range(2, n+1):
        if n % each == 0:
            result.append(each)
            if each == n:
                return result
            else:
                return factorize_helper(n, result)
            
print(factorize(128))            



