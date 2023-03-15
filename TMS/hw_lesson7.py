# Написать декоратор, который будет выводить в консоль
# имя функции, время вызова, и с какими параметрами она вызвана
# Примеры работы:
# add(1, 2) -> Функция add вызвана в 2023-03-14 22:21:53.986665 с позиционными параметрами (1, 2)
# add(a=1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986703 с именнованными параметрами {'a': 1, 'b': 2}
# add(1, b=2) -> Функция add вызвана в 2023-03-14 22:21:53.986718 с позиционными параметрами (1,) и с именнованными параметрами {'b': 2}

# Дополнительно (если есть время) добавить код для обработки такого примера:
# add() -> Функция add вызвана в 2023-03-14 22:25:46.942232 без параметров
import datetime
import  typing
from functools import wraps


def decorated(func: typing.Callable) -> typing.Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        if not args and not kwargs:
            print(f'Функция {func.__name__} вызвана в {datetime.datetime.now()} без параметров')
        elif not args and kwargs:
            print(f'Функция {func.__name__} вызвана в {datetime.datetime.now()} с именнованными параметрами {kwargs}')
        elif args  and kwargs:
            print(f'Функция {func.__name__} вызвана в {datetime.datetime.now()} с позиционными параметрами {args}'
                  f' и с именнованными параметрами {kwargs}')
        else:# args and not kwargs:
            print(f'Функция {func.__name__} вызвана в {datetime.datetime.now()} с позиционными параметрами {args}')
        return func(*args, **kwargs)
    return inner


@decorated
def add(*args, **kwargs):
    print(args, kwargs)
    return


add(2, 3, 4, b=0, c=9)
add(2, 3)
add(s=4, f=6)
add()

