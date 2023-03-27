import json

# Написать программу телефонная книга используя классы. Написать класс телефонной книги, который хранит
# список контактов. Он должен иметь возможность искать контакты по имени и по телефону (два разных метода),
# добавлять новые контакты и удалять контакты по имени или телефону. Контакты реализовать
# в виде объектов класса Контакт. Данные телефонной книги хранить в json файле.
file_name = 'my_contact.json'

class PhoneBook:
    def __init__(self, file_name: str):
        self.file_name = file_name


    with open(file_name, encoding='utf-8') as file:
        my_contact = json.load(file)
        print(my_contact)
    print('---------------------')


    def search_name(self, firstname: str) -> list:
        self.firstname = firstname
        return list(filter(lambda x: self.firstname in x['name'], PhoneBook.my_contact))


    def serch_phone(self, phone: str) -> list:
        self.phone = phone
        return list(filter(lambda x: self.phone in x['phone'], PhoneBook.my_contact))


    def write_json(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(PhoneBook.my_contact, file, indent=4)

    def add_new_contat(self, firstname, phone):
        self.firstname = firstname
        self.phone = phone
        if not any(list(map(lambda x: True if self.phone == x['phone'] and self.firstname == x['name'] else False,
                            PhoneBook.my_contact))):
            new_contact = {'name': self.firstname, 'phone': self.phone}
            PhoneBook.my_contact.append(new_contact)
            PhoneBook.write_json(self, file_name)


    def del_contact(self, firstname='', phone='') -> None:
        self.firstname = firstname
        self.phone = phone
        for index, value in enumerate(PhoneBook.my_contact):
            if self.firstname == value['name'] or self.phone == value['phone']:
                answer = input(f'Удалить текущий контакт {value} y/n: ')
                if answer == 'y':
                    PhoneBook.my_contact.pop(index)
            PhoneBook.write_json(self, file_name)

class Contact():
    def __init__(self, firstname, phone):
        self.firstname = firstname
        self.phone = phone



contact1 = Contact('Stephan', '+2342352352')
contact = PhoneBook(file_name)
contact.add_new_contat(contact1.firstname, contact1.phone)
name = input('Enter name for search: ')
print(contact.search_name(name))
print('--------------------')
phone = input('Enter phone for search: ')
print(contact.serch_phone(phone))
print('-------------------')

contact.del_contact(firstname='Lesha1')
contact.del_contact(phone='+2342352352')
# contact1.add_new_contat('Lesha1', '+3214121412411')
# contact1.del_contact(phone='+3214121412411')
# contact1.del_contact(firstname='Serhei')
print(PhoneBook.my_contact)
