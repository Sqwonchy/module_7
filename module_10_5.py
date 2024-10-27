from multiprocessing import Pool
from datetime import datetime


def read_info(name: str) -> list[str]:
    file_lines: list[str] = []
    with open(name, 'r') as file:
        while line_ := file.readline():
            file_lines.append(line_)
    return file_lines


filenames = [f'./file {number}.txt' for number in range(1, 5)]

start = datetime.now()
liner_data = []
for file in filenames:
    f = read_info(file)
    liner_data.append(f)

end = datetime.now()
result_1 = end - start

if __name__ == "__main__":
    print(f" результат линейной работы {result_1} секунды.")
    start = datetime.now()
    with Pool() as pool:
        resultat_data = pool.map(read_info, filenames)
    end = datetime.now()
    result_2 = end - start
    print(f" результат многопроцессорной работы {result_2} секунды.")
