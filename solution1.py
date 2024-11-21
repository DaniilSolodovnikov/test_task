"""Необходимо реализовать декоратор @strict Декоратор проверяет соответствие типов переданных в вызов функции
аргументов типам аргументов, объявленным в прототипе функции. (подсказка: аннотации типов аргументов можно получить
из атрибута объекта функции func.__annotations__ или с помощью модуля inspect) При несоответствии типов бросать
исключение TypeError Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float,
str Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию"""


def strict(func):
    """Декоратор, проверяющий соответствие типов аргументов."""

    def wrapper(*args, **kwargs):
        # Получаем аннотации типов из __annotations__
        arg_types = func.__annotations__
        # Проверяем, что все позиционные аргументы имеют правильные типы
        for i, arg in enumerate(args):
            if i < len(arg_types):  # Проверяем, есть ли аннотация для данного аргумента
                expected_type = arg_types[list(arg_types.keys())[i]]
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Неверный тип аргумента {i + 1} для функции {func.__name__}. "
                        f"Ожидалось {expected_type}, получено {type(arg)}"
                    )
        # Проверяем, что все именованные аргументы имеют правильные типы
        for name, value in kwargs.items():
            if name in arg_types:
                expected_type = arg_types[name]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Неверный тип аргумента {name} для функции {func.__name__}. "
                        f"Ожидалось {expected_type}, получено {type(value)}"
                    )
        # Вызываем исходную функцию, если типы аргументов верны
        return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
try:
    print(sum_two(1, 2.4))  # >>> TypeError
except TypeError as e:
    print(e)
