from random import choice

# Lambda-функция

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: True if x == y else False, first, second)))


# Замыкание

def get_advanced_writer(file_name):
    file = open(file_name, 'a', encoding='utf-8')

    def write_everything(*data_set):
        for i in data_set:
            file.write(f'{i}')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Метод __call__

class MysticBall:
    def __init__(self, *words):
        self.list = words

    def __call__(self):
        res = choice(self.list)
        return res


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
