def all_variants(text):
    for l in range(len(text)):
        yield text[l]
    for l in range(len(text)):
        if l != len(text) - 1:
            yield text[l] + text[l + 1]
    for l in range(len(text)+1):
        if l == len(text):
            yield text[l-3] + text[l-2] + text[l-1]

a = all_variants("abc")
for i in a:
    print(i)
