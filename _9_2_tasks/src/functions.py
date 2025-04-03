"""Напишите функцию, которая принимает имя файла и возвращает список имен,
содержащихся в файле.
Файл содержит имена на разных языках и может содержать знаки препинания вокруг имен,
пустые строки и цифры.
Функция должна удалить знаки препинания и цифры и возвращать только строки,
содержащие имя.
Сделайте новый коммит.
В отдельном коммите измените TXT-файл, сделав его меньше для простоты тестирования."""
import os


def name_str_from_file(file: str) -> list:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "../data/" + file)
    with open(file_path, 'r', encoding='utf-8') as f:
        name_list = f.readlines()
    new_list = []
    print(name_list)
    for name in name_list:
        new_name = ''
        for char in name:
            if char.isalpha():
                new_name += char
        if new_name:
            new_list.append(new_name)
    return new_list


if __name__ == '__main__':
    print(name_str_from_file('names.txt'))