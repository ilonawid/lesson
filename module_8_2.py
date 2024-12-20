def personal_sum(numbers):
    global true_numbers
    result = 0
    incorrect_data = 0
    try:
        true_numbers = 0
        for number in numbers:
            try:
                result += number
                true_numbers += 1
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы {number}')
                incorrect_data += 1
            my_tuple = (result, incorrect_data)
        return my_tuple
    except TypeError:
        return None


def calculate_average(numbers):
    sum = personal_sum(numbers)
    try:
        result = sum[0] / true_numbers
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average('1, 2, 3')}')  # Строка перебирается, но каждый символ - строковый тип

print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3

print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция

print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
