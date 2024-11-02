import os
import requests
from threading import Thread, Event
import queue
from PIL import Image
"""
программа берет рандомный инструмент и ищет по нему группу  
 создает папку с иконкой группы и ссылку на группу
 хотел изночально сделать поиск и скачивание  mp3 но с этим есть проблемы которые я пока что не смог сам решить
 p/s
 лучше такие вещи разбивать по модулям но я тогда запарюсь с отправкой через гитхаб домашки
"""

ACCES_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
URL_1 = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
URL_2 = "https://api.genius.com/search"
name_main_dir = "library of musical instruments"

# Создаем основную директорию
os.makedirs(name_main_dir, exist_ok=True)

queue_1 = queue.Queue()
st_ev = Event()
# counter_img = 3

def rand_mus_instrument():
    mus_instrument = requests.get(url=URL_1)
    return mus_instrument.json()


mus_instrument = rand_mus_instrument()
print(f'Сегодня инструмент для поиска группы это - {mus_instrument}.')


def save_img(img_url, file_name):
    try:
        response = requests.get(img_url, stream=True)
        if response.status_code == 200:
            with open(file_name, 'wb') as file:
                for chunk in response.iter_content(1024): # скачивание файла по частям.
                    file.write(chunk)
            # Изменение размера иконки группы
            with Image.open(file_name) as img:
                img = img.resize((100, 100))
                img.save(file_name)
        else:
            print(f'Загрузить изображение не удалось: код ответа сервера {response.status_code}')

    except Exception as e:
        print(f"Произошла ошибка при обработке изображения: {e}")


def save_url_group(file_group, text_): # создаем текст с сылкой на группу
    with open(file_group, "w", encoding='utf-8') as file:
        file.write(text_)


class SearchGroup(Thread):
    def __init__(self, mus_inst, queue_,st_ev):
        super().__init__()
        self.stop_event = st_ev
        self.queue = queue_
        self.mus_inst = mus_inst
    def run(self):
        take_ur = requests.get(url=URL_2, params={"access_token": ACCES_TOKEN, "q": self.mus_inst})# поиск по инструмент
        data = take_ur.json()
        hits = data['response']['hits']  # все хиты
        print(len(hits))
        if hits:
            for hit in hits:
                name_group = hit['result']['artist_names']
                img_group = hit['result']['header_image_thumbnail_url']
                url_group = hit['result']['url']
                group = (name_group, img_group, url_group)
                self.queue.put(group)

        else:
            print("Хм. никто не играет на данном инструменте....... \n Давайте поищем новый музыкальный инструмент... ")
            self.mus_inst = rand_mus_instrument()
            print(f"Новый инструмент для поиска музыкальных групп это {self.mus_inst} ")
            self.run()


class SaveGroup(Thread):
    def __init__(self, mus_inst, queue_,st_ev):
        super().__init__()
        self.counter = 1
        self.stop_event = st_ev
        self.queue = queue_
        self.name_dir = f"./{name_main_dir}/{mus_inst}"

        os.makedirs(self.name_dir, exist_ok=True)

    def run(self):
        while not self.stop_event.is_set():
            try:
                group = self.queue.get(timeout=5)  # Добавление таймаута

                dir_group = f'{self.name_dir}/group_{self.counter}'

                os.makedirs(dir_group, exist_ok=True) # Создание директории для группы

                name_img = f'{dir_group}/{group[0]}_icon.jpg'
                file_group = f'{dir_group}/{group[0]}_url.txt'
                text_ = f'Группа: {group[0]},\nСсылка на группу - {group[2]}'

                save_img(group[1], name_img)
                save_url_group(file_group, text_)
                self.counter += 1
                print(f'Найдена группа - {group[0]}')
            except queue.Empty:
                self.stop_event.set()
            except Exception as e:
                print(f'Ошибка при сохранении группы: {e}')



img_search = SearchGroup(mus_instrument, queue_1, st_ev)
img_save = SaveGroup(mus_instrument, queue_1, st_ev)

img_search.start()
img_save.start()

img_search.join()
img_save.join()
