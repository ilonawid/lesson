# team1_num = 5
# team2_num = 6
# score_1 = 40
# score_2 = 42
# team1_time = 1552.512
# team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = 'Победа команды Волшебники данных!'
#
# # Использование %:
# print('В команде Мастера кода участников: %s!' % str(team1_num))
# print('Итого сегодня в командах участников: %s и %s!' % (str(team1_num), str(team2_num)))
#
# # Использование format():
# print('Команда Волшебники данных решила задач: {}!'.format(score_2))
# print('Волшебники данных решили задачи за {}с!'.format(team1_time))
#
# # Использование f-строк:
# print(f'Команды решили {score_1} и {score_2} задач.')
# print(f'Результат битвы: {challenge_result}')
# print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

import os
import time
directory = '.'
for root, dirs, files in os.walk(directory): #обход каталога, путь к которому указывает переменная directory
    for file in files:
        filepath = os.path.join(root, file) # формирование полного пути к файлам
        filetime = os.path.getmtime(filepath) #  отображение времени последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath) # получение размера файла
        parent_dir = os.path.dirname(filepath) # получение родительской директории файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
       f'Родительская директория: {parent_dir}')
