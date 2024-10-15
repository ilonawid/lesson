calls = 0


def count_calls():
    global calls
    calls = int(calls) + 1
    return calls


string = input('Введите строку ')
tuple_ = tuple((len(string), string.upper(), string.lower()))
list_ = list(input('Введите список '))


def string_info(string):
    print(tuple_)
    count_calls()
    return tuple_


def is_contains(string, list_):
    if string in list_:
        print(True)
    else:
        print(False)
    count_calls()
    return


string_info(string)
is_contains(string, list_)
calls = count_calls() - 1
print(calls)
