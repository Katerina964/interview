class MyBaseClass:
    def my_method(self):
        print('Hello from MyBaseClass')

def monkey_patch():
    def new_method(self):
        print('Hello from new_method')
    MyBaseClass.my_method = new_method

monkey_patch()
obj = MyBaseClass()
obj.my_method()  # выведет "Hello from new_method"