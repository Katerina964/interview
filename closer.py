def my_function():
    static_var = 0

    def inner_function():
        nonlocal static_var
        static_var += 1
        return static_var

    return inner_function


# создаем объект функции, который использует статическую переменную
f = my_function()

# вызываем функцию несколько раз, чтобы увидеть изменение значения статической переменной
print(f())  # выводит 1
print(f())  # выводит 2
print(f())  # выводит 3
