"""Декоратор для функции sum_three """
def is_prime(func):
    def chek_num(*args):
        number = func(*args)
        cheker = True
        for i in range(2, number):
            if number % i:
                continue
            else:
                cheker = False
        if cheker:
            print(f"Число {number} простое")
        else:
            print(f"Число {number} не простое")
        return func(*args)
    return chek_num

@is_prime
def sum_three(num_1: int, num_2: int, num_3: int) -> int:
    result = num_1 + num_2 + num_3
    return result




result = sum_three(2, 3, 6)
print(result)