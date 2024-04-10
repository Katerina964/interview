def my_gen(n):
    for i in range(n):
        print(f"i before yield {i}")
        yield i
        print(f"N={n} i={i}")

for i in my_gen(3):
    print(i)

# second type for calling        
q = my_gen(3)
print(next(q))
print(next(q))
print(next(q))