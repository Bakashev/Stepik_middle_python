# # Задача 1: Дан словарь необходимо поменять местами ключ и значение
# # Решение через генераторы
# first_dict = {'a': 3, 'b': 4, 'n': 6}
# result_dict = {value: key for key, value in first_dict.items()}
# print(result_dict)


# Задача 2: факториал числа


# def get_factorial(number: int) -> int:
#     if number < 0:
#         return
#     if number in {0, 1}:
#         return 1
#     else:
#         return number * get_factorial(number-1)
#
#
# num = int(input('Enter number: '))
# print(get_factorial(num))


# Задача 3: Дан список чисел необходимо рассчитать сколько раз встречается каждое
# число
# list_number = [1, 2, 3, 4, 1, 2, 3, 41, 1, 2, 2, 2, 2]

# Использование in

# def count_number_dict(list_: list) -> dict:
#     result_dict2 = {}
#     for number in list_number:
#         if number in result_dict2:
#             result_dict2[number] += 1
#         else:
#             result_dict2[number] = 1
#     return result_dict2

# Использование get()

#
# def count_number_dict(list_: list) -> dict:
#     result_dict2 = {}
#     for number in list_number:
#         if result_dict2.get(number):
#             result_dict2[number] += 1
#         else:
#             result_dict2[number] = 1
#     return result_dict2
#
#
# print(count_number_dict(list_number))

