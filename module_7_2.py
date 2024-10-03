def custom_write(file_name, strings: list):
    strings_positions = dict()
    num = 0
    file = open(file_name,"a", encoding="utf-8")
    for string_ in strings:
        num += 1
        bite_pos = file.tell()
        position = (num,bite_pos)
        file.write(f"{string_}\n")
        strings_positions[position] = string_
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)