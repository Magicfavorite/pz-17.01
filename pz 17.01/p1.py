import random

# Создаем случайный список целых чисел
lst = [random.randint(-100, 100) for _ in range(10)]

# Выводим список чисел
print("Исходный список:")
print(lst)

# Сумма отрицательных чисел
neg_sum = sum([x for x in lst if x < 0])

# Сумма четных чисел
even_sum = sum([x for x in lst if x % 2 == 0])

# Сумма нечетных чисел
odd_sum = sum([x for x in lst if x % 2 != 0])

# Произведение элементов с индексами кратными 3
index_mul = 1
for i in range(len(lst)):
    if i % 3 == 0:
        index_mul *= lst[i]

# Произведение элементов между минимальным и максимальным элементом
min_index = lst.index(min(lst))
max_index = lst.index(max(lst))
min_max_mul = 1
if min_index < max_index:
    min_max_mul = 1
    for i in range(min_index + 1, max_index):
        min_max_mul *= lst[i]

# Сумма элементов, находящихся между первым и последним положительными элементами
pos_indexes = [i for i, x in enumerate(lst) if x > 0]
if len(pos_indexes) > 1:
    first_pos_index = pos_indexes[0]
    last_pos_index = pos_indexes[-1]
    sum_between_pos = sum(lst[first_pos_index+1:last_pos_index])
else:
    sum_between_pos = 0

# Выводим результаты
print(" Сумма отрицательных чисел:", neg_sum)
print(" Сумма четных чисел:", even_sum)
print(" Сумма нечетных чисел:", odd_sum)
print(" Произведение элементов с индексами кратными 3:", index_mul)
print(" Произведение элементов между минимальным и максимальным элементом:", min_max_mul)
print(" Сумма элементов, находящихся между первым и последним положительными элементами:", sum_between_pos)
