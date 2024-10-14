def apply_all_func(int_list, *functions) -> dict:
    for value in int_list:
        if isinstance(value, int) == False and isinstance(value, float) == False:
            raise TypeError("Функция принимает для работы в качестве первого аргумента только списки с числами")
    result = dict()
    try:
        for function_ in functions:
            result_fun = function_(int_list)
            result[function_.__name__] = result_fun
    except TypeError as exc:
        print("Во второй агрумент и далее можно передовать только функции")
    else:
        return result

def min(list_) -> int:
    sorted(list_)
    return list_[0]

def max(list_) -> int:
    sorted(list_)
    return list_[-1]

def len(list_):
    result = 0
    for value in list_:
        result += 1
    return result

def sum(list_):
    result = 0
    for value in list_:
        result += value
    return result

def sorted(list_):
    for i in range(len(list_) - 1):
        for h in range(len(list_) - 1 - i):
            if list_[h] > list_[h + 1]:
                list_[h], list_[h + 1] = list_[h + 1], list_[h]
    return list_

if __name__ == "__main__":
    dict_ = {1: "a"}
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
    print(apply_all_func([1, 2, 3], len, dict_))
    print(apply_all_func([6, "строка", 15, 9], len, sum, sorted))
