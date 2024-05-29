def fib_slice(n):
    fib_list = [1, 2]
    for each in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

def fib(n):
    a = 1
    b = 2
    fib_list = [1, 2]
    for eacn in range(2, n):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list    


def fib_rec(n, start=2, a=1, b=2, fib_list = [1, 2]):
    if start == n:
        return fib_list
    a, b = b, a + b
    fib_list.append(b)
    start +=1
    return fib_rec(n, start, a, b, fib_list)

# print(fib_slice(5))
# print(fib(5))
# print(fib_rec(5))

def pal(n):
    return str(n) == str(n)[::-1]

def pal_one(n):
    str_pal = ""
    str_n = str(n)
    while n > 0:
        str_pal += str(n % 10)
        n //= 10
    return str_pal == str_n

print(pal_one(1122113))



