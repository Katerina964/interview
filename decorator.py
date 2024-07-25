def decorator_hello(func):
    print("I am hello from outer func ")
    def inner(name, *args, **kwargs):
        func(name)
        return f"I am NEW result, {name}"
    return inner

@decorator_hello
def hello(name):
    return f"I am OLD result, {name}"


print(hello("Kate"))


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
print(y("David"))


decorator_example(say)("David")