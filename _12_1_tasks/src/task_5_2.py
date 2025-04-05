"""Напишите программу, которая будет принимать на вход JSON-файл
с данными о финансовых транзакциях,
фильтровать транзакции, совершенные в определенной валюте,
и сохранять отфильтрованные данные в новый JSON-файл.

Также напишите декоратор, который будет выводить в консоль статистику
по количеству отфильтрованных транзакций.
Статистика должна включать в себя количество отфильтрованных транзакций и
их суммарную стоимость."""
import json


def log_stat(func):
    """Декоратор, который будет выводить в консоль статистику
по количеству отфильтрованных транзакций"""
    def wrapper(*args, **kwargs):
        result_func = func(*args, **kwargs)
        count = len(result_func)
        sum_price = [abs(price['amount']) for price in result_func]
        print('Абсолютная суммарная стоимость: ', sum(sum_price))
        print('Количество отфильтрованных транзакций: ', count)
    return wrapper


@log_stat
def filtered_transactions(input_file, output_file, filter_by_currency='USD'):
    """Функция фильтрует данные в JSON файле по валюте, и сохраняет в новый файл результат"""
    with open('../data/' + input_file) as file:
        dict_data = json.load(file)
    filtered_data = [data for data in dict_data if data['currency'] == filter_by_currency]
    with open('../data/' + output_file, 'w') as file:
        json.dump(filtered_data, file, indent=4)
    return filtered_data


if __name__ == '__main__':
    filtered_transactions('transactions.json', 'result.json', 'USD')