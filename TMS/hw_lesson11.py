# Реализовать To Do список используя классы.
# В задаче хранить описание и приоритет (high, medium, low, по умолчанию low).
# Методы класса ToDoList:
# - добавить задачу
# - изменить описание задачи
# - изменить приоритет задачи
# - удалить задачу
# - вернуть список задач, отсортированный по приоритету (сначала высокий)
# - сохранить список в файл/загрузить из файла
from enum import Enum, IntEnum
import csv


class PrioritetEnum(IntEnum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Task:
    def __init__(self, name_task: str, task: str, prioriti_task: PrioritetEnum):
        self.name_task = name_task
        self.task = task
        self.prority = prioriti_task

    def __repr__(self):
        return f'{self.name_task},{self.task},{self.prority}'


class ToDoList:
    def __init__(self):
        self.to_do_list: list[Task] = []


    def add_list(self, task: Task):
        self.to_do_list.append(task)


    def edit_task(self, task: Task, new_task: str):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].task = new_task


    def edit_priorite(self, task: Task, new_prior: PrioritetEnum):
        if task in self.to_do_list:
            self.to_do_list[self.to_do_list.index(task)].prority = new_prior


    def del_task(self, task: Task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)


    def get_list(self) -> list[Task]:
        return sorted(self.to_do_list , key=lambda task: task.prority, reverse=True)


    def save_file(self):
        file_name = 'task.csv'
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name_task', 'task', 'prority'])
            result = [[element.name_task, element.task, element.prority] for element in self.to_do_list]
            writer.writerows(result)

task = Task('first', 'first task', PrioritetEnum.LOW)
task2 = Task('first2', 'first task', PrioritetEnum.MEDIUM)
task3 = Task('first3', 'first task', PrioritetEnum.HIGH)
task4 = Task('first4', 'first task', PrioritetEnum.LOW)

to_do_list = ToDoList()
to_do_list.get_list()
to_do_list.add_list(task)
to_do_list.add_list(task2)
to_do_list.add_list(task3)
to_do_list.add_list(task4)

print(to_do_list.get_list())
print(to_do_list.to_do_list)

to_do_list.edit_task(task3, 'edit task')
print(to_do_list.get_list())

to_do_list.del_task(task4)
print(to_do_list.get_list())

to_do_list.edit_priorite(task, PrioritetEnum.HIGH)
print(to_do_list.get_list())


to_do_list.save_file()














