def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for num in numbers:
        try:
            result += num
        except TypeError as exc:
            print(f"Неверный тип данных для подсчета суммы - {num}")
            incorrect_data += 1
    return (result,incorrect_data)
def calculate_average(numbers):
    try:
        sum_num = personal_sum(numbers)
        len_average = len(numbers) - sum_num[1]
        result = sum_num[0] / len_average
    except TypeError:
        print(f"В намберс записан некоректный тип данных - {type(numbers)}")
    except ZeroDivisionError:
        return 0
    else:
        return result
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать