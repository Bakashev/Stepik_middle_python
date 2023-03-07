# Дан список чисел.
# Написать функцию, которая вернет сумму только положительных элементов списка
# list_number = [3, -1, 2, 3, 6, 7]
#
#
# def sum_list(arg: list[int]) -> int:
#     sum_int = 0
#     for element in arg:
#         if element > 0:
#             sum_int += element
#     return sum_int
#
#
# print(sum_list(list_number))
# sum_list()

## Дан список чисел. Написать функцию, которая вернет минимальное значение из списка.
# (Конкретно в этой задаче встроенную функцию min не использовать)
# list_number = [3, -1, 2, 3, 6, 7]
#
#
# def min_number(arg: list[int]) -> int:
#     if len(arg) == 0: # if not arg
#         return None
#     min_num = arg[0]
#     for i in arg:
#         if min_num > i:
#             min_num = i
#     return min_num
#
#
# print(min_number([]))

# Написать функцию которая печатает числа от 0 до n, n - параметр.
# Если число делится на 3, вместо числа печатает fizz, если число делится на 5, вместо числа печатает buzz.
# Если число делится и на 3 и на 5, вместо числа печатает fizzbuzz


def print_numbers(arg: int) -> None:
    for i in range(arg):
        if i % 3 == 0 and arg % 5 == 0:
            print('fizzbuzz', end=' ')
        elif i % 3 == 0:
            print('fizz', end=' ')
        elif i % 5 == 0:
            print('buzz', end=' ')
        else:
            print(i, end=' ')


print_numbers(16)

