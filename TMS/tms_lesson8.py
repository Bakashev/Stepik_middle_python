# # работа с csv файлами, передача списка списков
# import json
# import random
# import csv
# filename = 'data_people.csv'
# my_list=[['tom', 23], ['slav', 23]]
# with open(filename, 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(my_list)
# # чтение файла csv
# with open(filename,'r', newline='') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0], '-', row[1])
#
# # Работа с csv файлами, передача словоря
# filename = 'dict_people.csv'
# dict_for_json= {'226238': ['Sergey', 23], '801950': ['Andrey', 14], '640235': ['vova', 19], '478654': ['Pavel', 39],
#                 '666082': ['Stas', 45], '952364': ['Stepan', 60]}
# with open(filename, 'w', newline='') as file:
#     colum = ('226238', 'id', 'name', 'age', 'phone')
#     writer = csv.DictWriter(file, fieldnames=colum)
#     writer.writeheader()
#     writer.writerow(dict_for_json)
# with open(filename, 'a', newline='') as file:
#     writer_name_header = csv.writer(file)
#     for key, value in dict_for_json.items():
#         print(key, value)
#         tmp_list = [key, value[0], value[1], '+37544' + str(random.randint(1000000, 9999999))]
#         writer_name_header.writerow(tmp_list)


# Задание 3. Создаьть словать в качестве ключа которого будет 6-ти значное число (id), а качестве значения кортеж
# состоящий из двух 2-ух эллементов - имя (str), возраст(int). Сделать около 5-6 элементов словаря. Записать данный
# словарь на диск в json файл
import csv
import json
# import random
# dict_for_json= {226238: ('Sergey', 23), 801950: ('Andrey', 14), 640235: ('vova', 19),
# 478654: ('Pavel', 39), 666082: ('Stas', 45), 952364: ('Stepan', 60)}
#
# with open('people.json', 'w', encoding='utf-8') as file_input:
#     json.dumps(dict_for_json, file_input, indent=4)
#     print(json.dumps(dict_for_json))
# # созадние словаря из json
with open('people.json', 'r', encoding='utf-8') as file_output:
    #read_dict_json = json.load(file_output)
    read_dict_json = json.loads(file_output)
    print(read_dict_json)
# for key, element in read_dict_json.items():
#     read_dict_json[key] = tuple(element)
#     print(element)
print(read_dict_json)



