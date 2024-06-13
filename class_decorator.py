from datetime import datetime
from os import path
import json


def check_cach(func):
    def wrapper(self, *agrs, **kwargs):
        if path.isfile("pet_cach.py"):
            time_dif = (
                datetime.now() - datetime.fromtimestamp(path.getmtime("pet_cach.py"))
            ).days
            if time_dif < 1:
                with open("pet_cach.py", "r") as cach_file:
                    result = json.load(cach_file)
            else:
                with open("pet_cach.py", "w") as cach_file: # TODO create func write cach
                    result = (
                        f"I am result from decorator func, {func(self)} {datetime.now()}"
                    )
                    cach_file.write(json.dumps(result))

        else:
            with open("pet_cach.py", "w") as cach_file:
                result = (
                    f"I am result from decorator func, {func(self)} {datetime.now()}"
                )
                cach_file.write(json.dumps(result))
        return result

    return wrapper


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @check_cach
    def pet_info(self):
        return f"I am {self.name}, I am {self.age} years old."


pet = Pet("Babe", 3)
print(pet.pet_info())


class MyDecorator:
    def __init__(self, function):
        self.function = function
     
    def __call__(self, *args, **kwargs):
 
        # We can add some code 
        # before function call
 
        self.function(*args, **kwargs)
 
        # We can also add some code
        # after function call.
     
 
# adding class decorator to the function
@MyDecorator
def function(name, message ='Hello'):
    print("{}, {}".format(message, name))
 
function("geeks_for_geeks", "hello")