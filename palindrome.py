def pal_one(n):
    list_pal = reversed(list(str(n)))
    palindrome = int(''.join(map(str, list_pal)))    
    if n == palindrome:
        return True
    else:
        return False
    
print(pal_one(333333333333))


def pal_two(n):
    palindrome = ""
    str_n = str(n)

    for i in range(1, len(str_n) +1):
        palindrome += str_n[-i]

    if n == int(palindrome):
        return True
    else:
        return False   
    
print(pal_two(112211))


def pal_three(n):
    palindrome = int(str(n)[::-1])

    if n == palindrome:
        return True
    else:
        return False

print(pal_three(333334))

def pal_for(n):
    palindrome = ""
    original_n = n

    for i in range(len(str(n))-1):
        palindrome += str(n % 10)
        n = int(n / 10)
    palindrome = int(palindrome + str(n))  

    if original_n == palindrome:
        return True
    else:
        return False 
    
print(pal_for(11122111))    