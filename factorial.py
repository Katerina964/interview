def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print (factorial(11))

def factorial_rec(n,  result=1, next_param=1):
    if next_param > n:
        return result

    result *= next_param
    return factorial_rec(n, result, next_param=next_param+1)

print(factorial_rec(5))