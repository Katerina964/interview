from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Пример использования filter() для отфильтровывания четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # выводит [2, 4, 6, 8, 10]

# Пример использования reduce() для нахождения суммы чисел от 1 до 10
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers) # выводит 55