"""Написать функцию, которая получает на вход два списка чисел
и возвращает новый список, содержащий только те числа,
которые встречаются в обоих списках.
Пример ввода:
[1, 2, 3, 4], [3, 4, 5, 6]

Пример вывода:
[3, 4]"""

def list_union(list1: list, list2: list) -> list:
    return [x for x in list1 if x in list2]
print(list_union([1, 2, 3, 4, 6], [3, 4, 5, 6]))