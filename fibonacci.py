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
    
def fib_rec(n, start=2, a=1, b=2, fib_list = [1, 2]):
    if start == n:
        return fib_list
    a, b = b, a + b
    fib_list.append(b)
    start +=1
    return fib_rec(n, start, a, b, fib_list)

print(fib_rec(15,  fib_list, start=2))
print(fib_list)

def fib(n):
    a = 1
    b = 2
    fib_list = [1, 2]
    for eacn in range(2, n):
        a, b = b, a + b
        fib_list.append(b)
    return fib_list


print(fib(15))
    


