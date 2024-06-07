class Pet:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def hello(self):
        return print(f"hello, {self.name}")

    def get_color(self):
        return print(f"I am {self.color}") 
    

class Dog(Pet):
    def __init__(self, name, color, size):
        super().__init__(name, color)
        self.size = size

    def get_size(self):
        return print(f"I am {self.size}")
    

dog = Dog("Frend", "white", "big")
dog.hello()
dog.get_color()
dog.get_size()