"""Напишите функцию, которая принимает имя файла и возвращает список имен,
содержащихся в файле.
Файл содержит имена на разных языках и может содержать знаки препинания вокруг имен,
пустые строки и цифры.
Функция должна удалить знаки препинания и цифры и возвращать только строки,
содержащие имя.
Сделайте новый коммит.
В отдельном коммите измените TXT-файл, сделав его меньше для простоты тестирования."""
import os
import re

CURRENT_DIR = os.path.dirname(__file__)


def name_str_from_file(file: str) -> list:
    """Функция очищения имен из файла и возвращения их в список"""
    file_path = os.path.join(CURRENT_DIR, "../data/" + file)
    with open(file_path, 'r', encoding='utf-8') as f:
        name_list = f.readlines()
    new_list = []
    for name in name_list:
        new_name = ''
        for char in name:
            if char.isalpha():
                new_name += char
        if new_name:
            new_list.append(new_name)
    return new_list


#if __name__ == '__main__':
#    print(name_str_from_file('names.txt'))

"""Напишите другие функции, позволяющие из списка имен получать только русские и английские 
и записывать эти имена в файл в отсортированном виде. 
В итоге программа должна считывать данные из исходного файла и формировать два файла 
с русскими и английскими именами, отсортированными по алфавиту. 
Новые файлы должны создаваться в папке data/. 
Всегда делайте точечные коммиты. После завершения разработки сделайте отмену коммита, 
в котором был урезан исходный файл, т. е. верните полный TXT-файл."""


def split_lang(list_names: list) -> None:
    file_path = os.path.join(CURRENT_DIR, "../data/")
    str_from_list = ' '.join(list_names)
    eng_names = re.findall(r'\w+',str_from_list , flags=re.ASCII)
    rus_names = list(set(list_names).difference(set(eng_names)))
    with open(file_path + 'rus_names.txt', 'w', encoding='utf-8') as file_ru:
        file_ru.write('\n'.join(sorted(rus_names)))
    with open(file_path + 'eng_names.txt', 'w', encoding='utf-8') as file_en:
        file_en.write('\n'.join(sorted(eng_names)))


if __name__ == '__main__':
        split_lang(name_str_from_file('names.txt'))