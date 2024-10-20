def all_variants(text: str):
    for len_1 in range(len(text)):
        for len_2 in range(len(text) - len_1):
            yield text[len_2:len_2 + len_1 + 1]

a = all_variants("Строка")
for i in a:
    print(i)