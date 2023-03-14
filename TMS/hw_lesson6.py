# # Задание 1. Написать lambda функцию определющая четное/ нечетное. Функция приимает
# # параметр число и если четное то выводит слово четное, если нет то нечетное
# import random
# list_number = [random.randint(-20, 20) for _ in range(10)]
# print(f'Список чисел: {list_number}')
# print(list(map(lambda num: 'четное' if num % 2 == 0 else 'нечетное', list_number)))
#
# # Задание 2. Дан список чисел. Вернуть список, где при помощи функции map каждое четное число,
# # переведео в строку
# import random
# list_number = [random.randint(-20, 20) for _ in range(10)]
# print(f'Список чисел: {list_number}')
# print(list(map(lambda num: str(num) if num % 2 == 0 else num, list_number)))
#
#
# # Задание 3. При помощи функции filter() из кортежа слов отфильтровать только те, которые являються
# # полиндромами
#
# words_tuple = ('шалаш', 'рюкзак', 'наган', 'дед', 'стол', 'заказ')
# print(list(filter(lambda word: word[:] == word[::-1], words_tuple)))

# # Задание 4 Написать декоратор к 2-м любым фунциям, которые бы считали и выводили время их выполнения
#
# #-------------------------первая реализация декоратора
# import typing
# from datetime import datetime
# from functools import wraps
#
#
# def decorate(func: typing.Callable) -> typing.Callable:
#     """
#     Декоратор к функции cost_tovar, доавляет к сумме веденный пользователем процент надбавки
#     :param func:
#     :return:
#     """
#     @ wraps(func)
#     def cost_product_nds(*args, **kwargs):
#
#         start = datetime.now()
#         nds = input('Enter percent: ')
#         if nds:
#             nds = int(nds)
#             sum_ = func(*args, **kwargs)
#             print(f'Сумма товара {kwargs["name"]} c добавкой {nds} = {sum_ + (sum_ * (nds / 100))}')
#             print(f'Время выполнения функции: - {datetime.now() - start}')
#         else:
#             print('Нет данных для оброботки')
#     return cost_product_nds
#
#
#
#
# @decorate
# def cost_product(*args, **kwargs) -> int:
#     """
#     Выводим количество умонженное на цену
#
#     :param kwargs: именнованные параметры name, kol, price
#     :return: kol * price
#     """
#     if 'kol' not in kwargs or 'price' not in kwargs:
#         return 0
#     else:
#         for key, value in kwargs.items():
#             if key == 'price':
#                 price = value
#             elif key == 'kol':
#                 kol = value
#         return kol * price
#
#
# cost_product(name='note', kol=2, price=120)
# print(cost_product.__doc__)
# cost_product(1, 2, 3, 4)
# cost_product()

# #-------------------------Вторая реализация декоратора
# from functools import wraps
# from typing import Callable
# from  datetime import datetime
#
#
# def decorate_fibonachi(func: Callable) -> Callable:
#     """
#     Декоратор в случае введенного отрицательного числа, спршивает надо ли провести расчет для отрицательного числа
#     и в случае утвердительного ответа осуществляет расчет, в случае отказа возвращает 0
#     :param func:
#     :return:
#     """
#
#
#
#
#     @wraps(func)
#     def func_factorial(num):
#         start = datetime.now()
#         if num < 0:
#             print(f'Число {num} отрицательное, хотите рассчитать фаткориал отрицального числа y\\n')
#             answer = input()
#             if answer == 'y':
#                 res = '-' + str(func(abs(num)))
#                 print(f'Время выполнения9 {datetime.now() - start}')
#                 return res
#             else:
#                 return 0
#
#         else:
#             res = func(num)
#             return res
#
#     return func_factorial
#
# @decorate_fibonachi
# def fibonachi_(num: int) -> int:
#     """
#     Функция принимает число и расситывает число фибоначи
#     :param num:
#     :return:
#     """
#     if num in {0, 1}:
#         return num
#     else:
#         return fibonachi_(num-2) + fibonachi_(num-1)
#
#
# print(fibonachi_(-30))


# # Задача 5. Сделать  функцию которая  на вход принимает строку. Анализирует ее исключительно методом isdigit()
# # и переводит строку в число. Функция умеет распозновать отрицательные числа и  десятичные дроби.
# # 6.7 - Вы ввели отрицательное дробное число: -6.7
# # 5 - Вы ввели положительное целое число: 5
# # 5.4r - Вы ввели не корректное число: 5.4r
# #-.777 - Вы ввели отрицательное дробное число: -0.777
#
#
# def transformation_str_to_int_float(number: str) -> None:
#     """
#     Функция принимает строку и преоброзовывает ее в число. Функция умеет распозновать отрицательные числа
#     и  десятичные дроби.
#     :param number: дробное или целое положительно или отрицательно число
#     :return: None
#     """
#     if number.isdigit():
#         print(f'{number} - Вы ввели положительное целое число: {int(number)}')
#     elif number[1:].isdigit() and number[0] == '-':
#         print(f'{number} - Вы ввели отрицательное целое число: {int(number)}')
#     elif not number.isdigit() and number[0] != '-':
#         count_point = 0
#         flag = True
#         for symbol in number:
#             if symbol.isdigit():
#                 continue
#             elif symbol == '.':
#                 count_point += 1
#             elif not symbol.isdigit():
#                 print(f'{number} - Вы ввели не корректное число: {number}')
#                 flag = False
#         if flag and count_point == 1:
#             print(f'{number} - Вы ввели положительное дробное число: {float(number)}')
#         else:
#             print(f'{number} - Вы ввели не корректное число: {number}')
#     elif not number[1:].isdigit() and number[0] == '-':
#         count_point = 0
#         flag = True
#         for symbol in number[1:]:
#             if symbol.isdigit():
#                 continue
#             elif symbol == '.' and count_point == 0:
#                 count_point += 1
#             elif not symbol.isdigit():
#                 flag = False
#         if flag and count_point == 1:
#             print(f'{number} - Вы ввели отрицательно дробное число: {float(number)}')
#         else:
#             print(f'{number} - Вы ввели не корректное число: {number}')
#
#
# number = input('Enter number: ')
# transformation_str_to_int_float(number)

# Задание 4 Написать декоратор к 2-м любым фунциям, которые бы считали и выводили время их выполнения

#-------------------------первая реализация декоратора
# import typing
# from datetime import datetime
# from functools import wraps
#
#
# def decorate_sum(func: typing.Callable) -> typing.Callable:
#     """
#     Декоратор к функции cost_tovar, доавляет к сумме веденный пользователем процент надбавки
#     :param func:
#     :return:
#     """
#     @ wraps(func)
#     def cost_product_nds(*args, **kwargs):
#
#         nds = input('Enter percent: ')
#         if nds:
#             nds = int(nds)
#             sum_ = func(*args, **kwargs)
#             if sum_ != 0:
#                 print(f'Сумма товара {kwargs["name"]} c добавкой {nds} = {sum_ + (sum_ * (nds / 100))}')
#             else:
#                 print('Нет данных для оброботки')
#         else:
#             print('Нет данных для оброботки')
#     return cost_product_nds
#
#
# def decorate_time(func: typing.Callable) -> typing.Callable:
#     @wraps(func)
#     def time(*args, **kwargs):
#         start = datetime.now()
#         func(*args, **kwargs)
#         print(f'Время выполнения: {datetime.now() - start}')
#     return time
#
# @decorate_time
# @decorate_sum
# def cost_product(*args, **kwargs) -> int:
#     """
#     Выводим количество умонженное на цену
#
#     :param kwargs: именнованные параметры name, kol, price
#     :return: kol * price
#     """
#     if 'kol' not in kwargs or 'price' not in kwargs:
#         return 0
#     else:
#         for key, value in kwargs.items():
#             if key == 'price':
#                 price = value
#             elif key == 'kol':
#                 kol = value
#         return kol * price
#
#
# cost_product(name='note', kol=2, price=120)
# print(cost_product.__doc__)
# cost_product(1, 2, 3, 4)
# cost_product()




