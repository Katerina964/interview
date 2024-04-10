def decorator_example(func):
    print("example")
    c = 1
    def wrapper(name, x=c):
        func(name)
        return print("inner_one", name,  x)
  
    return wrapper

# @decorator_example
def say(name):
    return print("HELLO")

# say("David")

y = decorator_example(say)
y("David")


decorator_example(say)("David")