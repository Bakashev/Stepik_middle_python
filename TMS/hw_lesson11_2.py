# Написать класс банковский аккаунт. Хранить баланс, и историю операций над аккаунтом.
# Добавить методы пополнения баланса и снятия средств с баланса. Класс для истории должен
# хранить операцию (снятие или пополнение), сумму, дату и время операции.
# Создать экземпляр банковского аккаунта и проверить его работу.
from  dataclasses import dataclass
from datetime import datetime
from enum import Enum
import time


class OperationsEnum(Enum):
    TOP = 'Пополнение'
    REMOVE = 'Снятие'



class History:
    def __init__(self, operation: OperationsEnum, number: float, date_: datetime) -> None:
        self.opertion = operation
        self.sum = number
        self.date = date_

    def __repr__(self):
        return f'{self.opertion}, {self.sum}, {self.date}'


# @dataclass
# class BankAccount:
#     _balans: float = 0
#     history_operations: list[] = []
#     name: str = ''

class BankAccount:
    def __init__(self, balans: float, name: str):
        self._balans = balans
        self.name = name
        self.history_operations: list[History] = []

    def __repr__(self):
        return f'Имя - {self.name}. Баланс счета - {self._balans}'



class OperationsAccount:

    def __init__(self) -> None:
        self.account: list[BankAccount] = []

    def add_acount(self, bank_account: BankAccount):
        self.account.append(bank_account)

    @property
    def _balans(self, bank_account: BankAccount):
        if bank_account in self.account:
            return  f'Баланс счета {bank_account.number_account}: {bank_account._balans}'


    def top_up_balans(self, number: int, bank_account: BankAccount) -> None:
        if bank_account in self.account:
            start = datetime.now()
            history = History(OperationsEnum.TOP, number, start)
            bank_account.history_operations.append(history)
            self.account[self.account.index(bank_account)]._balans += number


    def remove_from_balans(self, number: int, bank_account: BankAccount) -> None:
        if bank_account in self.account:
            time.sleep(1)
            start = datetime.now()
            history = History(OperationsEnum.REMOVE, number, start)
            bank_account.history_operations.append(history)
            self.account[self.account.index(bank_account)]._balans -= number



client = BankAccount(100, 'Sergey')
print(client)
operation = OperationsAccount()
operation.add_acount(client)
operation.top_up_balans(20, client)
operation.top_up_balans(20, client)
operation.remove_from_balans(100, client)
print(client.history_operations)
print(f'остаток на счете: {client._balans}')
print(client)
print('__________________________')
client2 =BankAccount(1000, 'Andrey')
operation.add_acount(client2)
print(client2)
operation.top_up_balans(200, client2)
operation.remove_from_balans(199, client2)
operation.top_up_balans(100, client2)
print(client2.history_operations)
print(f'остаток на счете: {client2._balans}')
print(client2)
print('__________')

print(operation.account)







