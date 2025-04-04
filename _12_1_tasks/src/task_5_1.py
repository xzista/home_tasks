"""Задача 1
Напишите функцию generate_users(first_names, last_names, cities),
которая будет генерировать случайных пользователей.
Функция должна возвращать генератор,
который будет выдавать каждого пользователя по одному в виде словаря.

Каждый пользователь должен иметь следующие данные:

    first_name — имя из списка first_names;
    last_name — фамилия из списка last_names;
    age — возраст от 18 до 65 лет;
    city — город из списка cities.

Сгенерируйте группу пользователей и выведите ее списком в консоль в формате JSON."""
import json
from random import choice, randint


def generate_users(first_names: list, last_names: list, cities: list):
    """Функция генерации случайных пользователей на основе выданных списков"""
    while True:
        user = {
            "first_name": choice(first_names),
            "last_name":  choice(last_names),
            "age": randint(18, 65),
            "city": choice(cities)
        }
        yield user



if __name__ == '__main__':
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
    first_names = ['John', 'Jane', 'Mark', 'Emily', 'Michael', 'Sarah']
    last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Lee', 'Wilson']

    users = generate_users(first_names, last_names, cities)
    user_group_1 = [next(users) for i in range(4)]
    user_group_2 = [next(users) for i in range(6)]
    print('User group #1', json.dumps(user_group_1),
          'User group #2', json.dumps(user_group_2), sep='\n')