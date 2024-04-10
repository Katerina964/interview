def pal_one(n):
    list_pal = reversed(list(str(n)))
    palindrome = int(''.join(map(str, list_pal)))    
    return n == palindrome

print(pal_one(333333333333))

def pal_two(n):
    palindrome = ""
    str_n = str(n)

    for i in range(1, len(str_n) +1):
        palindrome += str_n[-i]

    return n == int(palindrome)
 
    
print(pal_two(112211))


def pal_three(n):
    palindrome = int(str(n)[::-1])

    return n == palindrome

print(pal_three(333334))

def pal_for(n):
    palindrome = ""
    original_n = n

    for i in range(len(str(n))-1):
        palindrome += str(n % 10)
        n = n // 10

    palindrome = int(palindrome + str(n))  
    return original_n == palindrome
    
print(pal_for(11122111))

def pal(a):
    c = a
    b = 0

    while c >= 1:
        b = (b + c % 10) * 10
        c = c // 10

    return a == b / 10

print(pal(333))