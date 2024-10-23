from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemis_varior = 100
        self.day = 0

    def run(self):
        print(f"{self.name} на нас напали!")
        while self.enemis_varior > 0:
            self.enemis_varior -= self.power
            sleep(1)
            self.day += 1
            print(f"{self.name} сражается {self.day} дней(дня!) осталось {self.enemis_varior} врагов.")
        print(f"{self.name} одержал победу спустя {self.day} дней(дня!)")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
sleep(0.1)
second_knight.start()

first_knight.join()
second_knight.join()