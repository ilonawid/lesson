calls = 0


def count_calls():
    global calls
    calls = int(calls) + 1
    return calls


def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [string.upper() for string in list_to_search]


def string_info(string):
    a = string
    tuple_ = (len(a), a.upper(), a.lower())
    count_calls()
    return tuple_


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
