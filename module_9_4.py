"""Лямбда_функция_______________________________________________________"""
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

"""Замыкание____________________________________________________________"""

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for text in data_set:
                file.write(str(text))
                file.write("\n")

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 42, 'в', 'списке'])

"""Метод __call__ для_вызова_класса_как_функции________________________________________"""
from random import choice
class MysticBall:
    def __init__(self, *words):
        self.words = list(words)

    def __call__(self) -> str:
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное','может_быть',"как_нибудь", "где_нибудь", "почему_нибудь")
print(first_ball())
print(first_ball())
print(first_ball())
