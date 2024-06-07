def fibonacci(length):
    fib_list = [0, 1]
    for each in range(2, length):
        fib_list.append(fib_list[-1] + fib_list[-2])

    return fib_list

print(fibonacci(15))

# recursion
fib_list = [0, 1]

def fib_rec(length,  fib_list, start=2):
    if start < length:
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_rec(length, fib_list, start+1) 

    else:
        return fib_list 
    
def fib_rec(n, a=0, b=1, fib_list=[0, 1]):

    if len(fib_list) == n:
        return fib_list

    a, b = b, a + b
    fib_list.append(b)
    return fib_rec(n, a, b, fib_list)

print(fib_rec(15))
print(fib_list)

def fib(n, a=0, b=1):
    fib_list = [a, b]
    for eacn in range(2, n):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list


print(fib(15))
    


