# 1
# Написать функцию, которая проверяет является ли целое число четным.
# Функция возвращает True, если число четное, False если нет.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.
# Ввод и вывод результата производится вне функции проверки
answer = input('Enter number: ')


def control_even(arg: str) -> bool:
    if arg.isdigit():   # O(n)
        arg = int(arg)
        if arg % 2 == 0:
            return True
        else:
            return False
    else:
        err = 'Введенные данные не являются целым числом'
        return err


print(control_even(answer))
# 2
# Написать функцию, которая принимает число n и выводит числа от 0 до n.
# Если число является четным, вывести квадрат числа, вместо числа.
# Для проверки на четность использовать функцию из задания 1.
# Если число делится на 7 и на 4 одновременно, процесс останавливается.
# Если пользователь ввел не число, вывести ошибку, что введенные данные не являются числом.

answer = input('Enter number: ')


def print_number(arg: str) -> None:
    if arg.isdigit():
        for element in range(int(arg)):         #O(n)
            if element % 7 == 0 and element % 4 == 0 and element != 0:
                break
            elif control_even(str(element)):
                print(element ** 2, end=' ')
            else:
                print(element, end=' ')
    else:
        print('Введенные данные не являются целым числом')


print_number(answer)
