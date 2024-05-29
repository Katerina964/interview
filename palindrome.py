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
    return int(str(n)[::-1]) == n

def pal_five(n):    
    return str(n) == str(n)[::-1]

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

def pal(n):
    str_pal = ""
    str_n = str(n)
    while n > 0:
        str_pal += str(n % 10)
        n //= 10
    return str_pal == str_n

print(pal(333))