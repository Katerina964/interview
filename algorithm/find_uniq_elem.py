def find_elem(n: list):
    for i in n:
        if i in n:
            n.remove(i)
            if i not in n:
                return i
            
    return

n = [1, 1, 2, 2, 5]
print(find_elem(n))