# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

from collections.abc import Hashable

res = {'a': 1984, 'b': 'QUEEN', 'c': 3.14, 'd': ('To be', 'or', 'Not to be')}

def args_to_dict(**kwargs) -> dict:
    return {y:x for x,y in kwargs.items()}

print('\nВыводим значения:\n', (args_to_dict(**res)))