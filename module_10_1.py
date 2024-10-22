from time import sleep
from threading import Thread
from datetime import datetime

start_time_func = datetime.now()
def write_words(word_count, file_name):
    number_line = 0
    for lines in range(word_count):
        number_line += 1
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"Какое то слово № {number_line} \n")
        sleep(0.1)
    print(f"Завершилась запись в файл {file_name}.")

all_doc = [(10, "example1.txt"), (30, "example2.txt"), (200, "example3.txt"), (100, "example4.txt")]

for doc in all_doc:
    write_words(doc[0], doc[1])

end_time_func = datetime.now()
result_time_for_function = end_time_func - start_time_func
print(f"Вермя работы функций {result_time_for_function}!")

start_time_thread = datetime.now()
all_thread = []
for doc in all_doc:
    all_thread.append(Thread(target=write_words, args=doc))

for thread in all_thread:
    thread.start()

for thread in all_thread:
    thread.join()

end_time_thread = datetime.now()
result_time_for_thread = end_time_thread - start_time_thread
print(f"Вермя работы потоков {result_time_for_thread}!")
