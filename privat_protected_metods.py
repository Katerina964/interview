class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__privat_attribute = "privat attribute"

    def __privat_method(self):
        print(self.__privat_attribute)
        return print("privat method")

    def _protected_method(self):
        return print("protected method")

    def call_privat_protected_methods(self):
        self._protected_method()
        self.__privat_method()

    def __str__(self):
        return print("PET")

pet = Pet("Babe", 3)
pet.call_privat_protected_methods()  # protected method  privat method 
pet._protected_method() # protected method
pet.__str__() # available

# call with new method_name
pet._Pet__privat_method() # privat method
print(pet._Pet__privat_attribute)

# Pet.__privat_method() #type object 'Pet' has no attribute '__privat_method'

class Cat(Pet):

    # should call only if need to change, defauld wil call parent's  __init__
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def hello():
        print("hello")

cat = Cat("Businka", 4, "white")
print(cat.name)
print(cat._Pet__privat_attribute)
