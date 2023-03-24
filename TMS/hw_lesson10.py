# # Созадть родительский класс Auto, у которого есть атрибуты: brand, age, color, mark, weight. А также методы: move
# # birthday, stop. Методы move и stop выводят сообщения на экран "move" , "stop", а birthday увеличивает age на 1.
# # Атрибуты класа, brand, age и mark являются обязательными при объявлении объекта

import datetime
import json
import time

# class Auto:
#
#
#     def __init__(self, brand: str, age: int, mark: str, color=None, weight=None) -> None:
#         self.brand = brand
#         self.age = age
#         self.mark = mark
#         self.color = color
#         self.weight = weight
#
#
#     def move(self) -> None:
#         print('move')
#
#
#     def stop(self) -> None:
#         print('stop')
#
#
#     def birthday(self) -> None:
#         self.age += 1
#
#
# car = Auto('hyundai', 10, 'accent')
# print(car.age)
# car.move()
# car.stop()
# car.birthday()
# print(car.age)
#
# # Создать два класса Truck и Car, которые являются наследниками класса Auto. Класс Truck имеет дополнительный
# # обязательный атрибут max_load. Переопределенный метод move, Перед появлением надписи 'move' выводит
# # надпись "attention"? его реализацию сделать при помощи оператора super. А также дополнительный метод load.
# # При его вызове происходит пауза 1 сек, затем выдается сообщение load и снова пауза 1 сек. Класс Car имеет
# # дополнительный обязательный атрибут max_speed и при вызове метода move должна появиться надпись
# # "max speed is <max_spped>". Создать по два объекта для каждого из классов Truck  и Car, проверить
# # все их методы и атрибуты
#
# class Truck(Auto):
#
#
#     def __init__(self, brand: str, age: int, mark: str, max_load: int, color=None, weight=None) -> None:
#         super().__init__(brand, age, mark, color=None, weight=None)
#         self.max_load = max_load
#
#     def move(self) -> None:
#         print('Attention?')
#         super().move()
#
#
#     def load(self):
#         print(datetime.datetime.now())
#         time.sleep(1)
#         print('load')
#         time.sleep(1)
#         print(datetime.datetime.now())
#
# class Car(Auto):
#
#
#     def __init__(self, brand: str, age: int, mark: str, max_speed: int, color=None, weight=None) -> None:
#         super().__init__(brand, age, mark, color=None, weight=None)
#         self.max_speed = max_speed
#
#
#     def move(self) -> None:
#         print(f'max_speed is {self.max_speed}')
#
#
# auto1 = Truck('MAZ', 10, "MC1", 20)
# auto2 = Truck('ZIL', 2, 'ZX', 5)
# list_truck = [auto1, auto2]
# for auto in list_truck:
#     print('------------')
#     print(auto.brand, auto.age, auto.mark, auto.max_load, auto.color, auto.weight)
#     auto.move()
#     auto.stop()
#     auto.birthday()
#     print(f'new age = {auto.age}')
#     auto.load()
#
# auto3 = Car('hyundai', 10, 'accent', 160)
# auto4 = Car('bmv', 4, 'X5', 230)
# list_car = [auto3, auto4]
# for auto in list_car:
#     print('------------')
#     print(auto.brand, auto.age, auto.mark, auto.max_speed, auto.color, auto.weight)
#     auto.move()
#     auto.stop()
#     auto.birthday()
#     print(f'new age = {auto.age}')

# Написать программу телефонная книга используя классы. Написать класс телефонной книги, который хранит
# список контактов. Он должен иметь возможность искать контакты по имени и по телефону (два разных метода),
# добавлять новые контакты и удалять контакты по имени или телефону. Контакты реализовать
# в виде объектов класса Контакт. Данные телефонной книги хранить в json файле.

class PhoneBook:
    file_name = 'my_contact'
    with open(file_name, encoding='utf') as file:
        my_contact = json.load(file)
    print(my_contact)
    print('---------------------')
    def __init__(self):
        pass


    def search_name(self, firstname: str) -> list:
        self.firstname = firstname
        return list(filter(lambda x: self.firstname in x['name'], PhoneBook.my_contact))


    def serch_phone(self, phone: str) -> list:
        self.phone = phone
        return list(filter(lambda x: self.phone in x['phone'], PhoneBook.my_contact))

class Contact(PhoneBook):
    def __init__(self):
        pass


    def add_new_contat(self, firstname, phone):
        self.firstname = firstname
        self.phone = phone
        if not any(list(map(lambda x: True if self.phone == x['phone'] and self.firstname == x['name'] else False,
                            PhoneBook.my_contact))):
            new_contact = {'name': self.firstname, 'phone': self.phone}
            PhoneBook.my_contact.append(new_contact)
            with open(PhoneBook.file_name, 'w', encoding='utf-8') as file:
                json.dump(PhoneBook.my_contact, file, indent=4)


    def del_contact_by_name(self, firstname):
        self.firstname = firstname



contact = PhoneBook()
print(contact.search_name('Serg'))
print('--------------------')
print(contact.serch_phone('+1'))
print('-------------------')
contact1 = Contact()
contact1.add_new_contat('Lesha1', '+3214121412411')

print(PhoneBook.my_contact)
# file_name = 'my_contact'
# dict_contact = {
#                 'name': 'Andrey',
#                 'phone': '+121782648'
#                 }
# dict_contact2 = {
#                 'name': 'Sergey',
#                 'phone': '+1239482348'
#                 }
# phone_book = [dict_contact, dict_contact2]
# with open(file_name, 'w', encoding='utf-8') as file:
#     json.dump(phone_book, file, indent=4)
