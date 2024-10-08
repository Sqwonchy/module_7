
def add_everything_up(a,b):
    try:
        result = a + b
        if isinstance(result,float):
            result = round(result,3)
    except:
        result = str(a) + str(b)
    finally:
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up(123, 7))
