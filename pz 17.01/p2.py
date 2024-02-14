import random

# Создаем случайный список целых чисел
lst = [random.randint(-100, 100) for _ in range(10)]

# Создаем список целых, содержащий только четные числа
even_nums = [x for x in lst if x % 2 == 0]

# Создаем список целых, содержащий только нечетные числа
odd_nums = [x for x in lst if x % 2 != 0]

# Создаем список целых, содержащий только отрицательные числа
negative_nums = [x for x in lst if x < 0]

# Создаем список целых, содержащий только положительные числа
positive_nums = [x for x in lst if x > 0]

print("Исходный список: ", lst)
print("Список четных чисел: ", even_nums)
print("Список нечетных чисел: ", odd_nums)
print("Список отрицательных чисел: ", negative_nums)
print("Список положительных чисел: ", positive_nums)
