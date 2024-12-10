# Дано списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings, где длина строк не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]
# 2. Список пар слов (кортежей) одинаковой длины
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]
# 3. Словарь, где строка - ключ, длина строки - значение, для строк с чётной длиной
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)

# first_result: Списковая сборка, которая проходит по каждому элементу s в списке first_strings.
# Если длина строки s больше или равна 5, добавляется длина этой строки в новый список.
#
# second_result: Двойная списковая сборка, которая создает кортежи из строк из first_strings
# и second_strings только в том случае, если длины этих строк равны.
#
# third_result: Словарная сборка, которая объединяет оба списка
# (first_strings и second_strings). В качестве ключа используется строка s,
# а в качестве значения — её длина, если длина строки четная.
#
# Пример вывода:
#
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'),
# ('Monitors', 'Computer'), ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4,
# 'Java': 4, 'Computer': 8}
