"""Напишите декоратор, который проверяет,
что все числа, возвращаемые декорируемой функцией,
являются целыми, и округляет их до целых, если это не так."""


def decorate_check_integers(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) == int:
            return result
        elif type(result) in [list, tuple]:
            return type(result), [round(x) if type(x) == float else x for x in result]
        elif type(result) == float:
            return round(result)
        elif type(result) == str:
            if "." in result:
                new_result = result.replace(".", "")
                if new_result.isdigit():
                    return type(result), str(round(float(result)))
            else:
                return result
        else:
            return result

    return wrapper


@decorate_check_integers
def numbers():
    return ["12.6", 12.2, 12.6]


if __name__ == "__main__":
    print(numbers())
