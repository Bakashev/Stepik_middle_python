import json
import random


json_file_name = 'matrix.json'
number_line = int(input('Enter number of line: '))
number_column = int(input('Enter number of column: '))
list_number_random = [[random.randint(20, 40) for _ in range(number_line)] for _ in range(number_column)]
#dict_list = {index: value for index, value in enumerate(list_number_random)}
for row in list_number_random:
    print(row)
with open(json_file_name, 'w', encoding='utf-8') as file:
    json.dump(list_number_random, file, indent=4)



