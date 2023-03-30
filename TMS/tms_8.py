# 1
# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину.
words = """Вечерело
Жужжали мухи
Светил фонарик
Кипела вода в чайнике
Венера зажглась на небе
Деревья шумели
Тучи разошлись
Листва зеленела"""
with open('article.txt', 'w', encoding='utf-8') as file:
         file.write(words.replace('\n', ' '))

def longest_words(file_: str) -> str:
    with open(file_, encoding='utf-8') as file:
        list_file = file.read().split(' ')
        max_len = len(list_file[0])
        for element in list_file[1:]:
            if max_len < len(element):
                max_len = len(element)
        filter_ = list(filter(lambda word: max_len == len(word), list_file))
        return filter_

print(longest_words('article.txt'))


# 2
# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file
# и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела