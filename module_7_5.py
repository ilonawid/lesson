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