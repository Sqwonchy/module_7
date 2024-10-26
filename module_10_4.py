from datetime import datetime
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:
    def __init__(self, *args):
        self.queue = Queue()
        self.tables = args

    def chek(self):
        for table in self.tables:
            if table.guest == None:
                return table
        return None

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.chek()
            if table:
                table.guest = guest.name
                print(f"{guest.name} сел(а) за стол номер {table.number}")
                guest.start()
            else:
                print(f"{guest.name} в очереди")
                self.queue.put(guest)

    def discuss_guests(self):
        while not self.queue.empty() or self.chek():
            for table in tables:
                for guest in guests:
                    if guest.name == table.guest:
                        if guest.is_alive() == False:
                            print(f"{guest.name} покушал(-а) и ушёл(ушла) и Стол номер {table.number} свободен")
                            table.guest = None
                            if not self.queue.empty():
                                guest = self.queue.get()
                                print(f"{guest.name} вышел(-ла) из очереди и сел(-а)pf стол номер {table.number}")
                                table.guest = guest.name
                                guest.start()

if __name__ == "__main__":
    start_ = datetime.now()
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
    end = datetime.now()
    res = end - start_
    # Конец работы и подсчет времени работы (от себя добавил)
    print(f"Работа кафе на сегодня закончилась общее время работы кафе: {res}")
