import csv
import json
import random

# # Задача 1. Декодировать в строку байтовое значение b'r\xc3\xa9sum\xc3\xa9'. Затем результат преоброзовать в байтовый
# #  вид в кодировке 'Latin1' и затем результат снова декодировать в строку (рузультаты всех преоброзований выводить
# #  на экран)
# first_item = b'r\xc3\xa9sum\xc3\xa9'
# print(f'Byte item:  {first_item}')
# decode_utf = first_item.decode('utf-8')
# print(f'Decoding to str format utf-8: {decode_utf}')
# code_item_latin = decode_utf.encode('Latin1')
# print(f'Byte item format Latin: {code_item_latin}')
#
#
# # Задание 2. Ввести с клавиатуры 4 строки и сохранить их в разные переменные. Создать файл и записать их в первые две
# # строки и закрыть файл. Затем открыть файл на редактирование и записать отсавшиеся две строки. В итоговом файле
# # должно быть 4 строки, каждая должна начинаться с новой строки
# # Задание 2. Ввести с клавиатуры 4 строки и сохранить их в разные переменные. Создать файл и записать их в первые две
# # строки и закрыть файл. Затем открыть файл на редактирование и записать отсавшиеся две строки. В итоговом файле
# # должно быть 4 строки, каждая должна начинаться с новой строки
list_string = [input('Enter string: ') + '\n' for _ in range(4)]
print(list_string)
file_name = 'four_string.txt'
first_str = list_string[0]
second_str = list_string[1]
third_str = list_string[2]
four_str = list_string[3]
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(first_str)
    file.write(second_str)
with open(file_name, 'a', encoding='utf-8') as file:
    file.write(third_str)
    file.write(four_str)

# Задание 3. Создаьть словать в качестве ключа которого будет 6-ти значное число (id), а качестве значения кортеж
# состоящий из двух 2-ух эллементов - имя (str), возраст(int). Сделать около 5-6 элементов словаря. Записать данный
# словарь на диск в json файл



file_name = 'people.json'
dict_for_json= {226238: ('Sergey', 23), 801950: ('Andrey', 14), 640235: ('vova', 19),
                 478654: ('Pavel', 39), 666082: ('Stas', 45), 952364: ('Stepan', 60)}

with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(dict_for_json, file, indent=4)

# прочитать сохраненный json-файл и записать данные на диск в csv-файл, первой строкой котороой озоглавить каждый
# столбец и добавить новый столбец телефон



with open('people.json') as file:
    people_info = json.load(file)
    file_name_csv = 'people_and_phone.csv'
    with open(file_name_csv, 'w', encoding='utf-8', newline='') as file_csv:
        header = ['id', 'name', 'age', 'phone']
        writer = csv.writer(file_csv)
        writer.writerow(header)
        for key, element in people_info.items():
            writer.writerow([key, element[0], element[1], f'+37544{random.randint(1000000,9999999)}'])