first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
first_result = (len(my_tuple[0]) - len(my_tuple[1]) for my_tuple in list(zip(first, second))
                if len(my_tuple[0]) != len(my_tuple[1]))
second_result = (True if len(first[string]) == len(second[string]) and len(first) == len(second)
                 else False for string in range(0, len(first)))

print(list(first_result))
print(list(second_result))
