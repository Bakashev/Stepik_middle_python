# Созадть родительский класс Auto, у которого есть атрибуты: brand, age, color, mark, weight. А также методы: move
# birthday, stop. Методы move и stop выводят сообщения на экран "move" , "stop", а birthday увеличивает age на 1.
# Атрибуты класа, brand, age и mark являются обязательными при объявлении объекта

class Auto:


    def __init__(self, brand: str, age: int, mark: str, color=None, weight=None) -> None:
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight


    def move(self) -> None:
        print('move')


    def stop(self) -> None:
        print('stop')


    def birthday(self) -> None:
        self.age += 1


car = Auto('hyundai', 10, 'accent')
print(car.age)
car.move()
car.stop()
car.birthday()
print(car.age)

