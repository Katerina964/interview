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

print(fib_rec(15,  fib_list, start=2))
print(fib_list)