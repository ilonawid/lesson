def all_variants(text: str):
    length = len(text)
    for l in range(1, length + 1):
        for i in range(length - l + 1):
            yield text[i:i + l]


a = all_variants("abc")
for i in a:
    print(i)
