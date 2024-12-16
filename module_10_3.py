import threading
import random
import time
from threading import Thread, Lock
from time import sleep


class Bank(Thread):

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for tran in range(100):
            number = random.randint(50, 500)
            self.balance += number
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'"Пополнение: {number}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for tran in range(100):
            number = random.randint(50, 500)
            print(f'Запрос на {number}')
            if number <= self.balance:
                self.balance -= number
                print(f'Снятие: {number}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))

th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()

th2.start()

th1.join()

th2.join()
print(f'Итоговый баланс: {bk.balance}')