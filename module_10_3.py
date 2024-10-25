from threading import Thread, Lock
from random import  randint
from time import sleep

lock_1 = Lock()
lock_2 = Lock()
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
    def deposit(self):
        for i in range(10):
            if self.lock.locked():
                self.lock.release()
            coin = randint(50,500)
            self.balance += coin
            print(f"Пополнение: {coin}. Баланс: {self.balance}")

            sleep(0.001)
    def take(self):
        for i in range(10):

            coin = randint(50, 500)
            print(f"Запрос на {coin}.")
            if coin <= self.balance:
                self.balance -= coin
                print(f"Снятие: {coin}. Баланс: {self.balance}")
            else:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)
bk = Bank()
th_1 = Thread(target=Bank.deposit, args=(bk,))
th_2 = Thread(target=Bank.take, args=(bk,))

th_1.start()
th_2.start()
th_1.join()
th_2.join()
print(f"Итоговый баланс {bk.balance}")


