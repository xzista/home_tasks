"""Написать функцию, которая получает на вход два списка чисел
 и возвращает новый список, содержащий только те числа,
  которые есть только в одном из списков.
Пример ввода:
[1, 2, 3, 4], [3, 4, 5, 6]

Пример вывода:
[1, 2, 5, 6]"""


def list_difference(list1: list[int], list2: list[int]) -> list[int]:
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]


if __name__ == "__main__":
    print(list_difference([1, 2, 3, 4], [3, 4, 5, 6]))
