from time import sleep
from time import time
import threading


def wite_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as name:
        for number in range(1, word_count + 1):
            name.write(f'Какое-то слово № {number}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start = time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
finish = time()
print(finish - start)
start = time()
thread = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
thread.start()
thread = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
thread.start()
thread = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
thread.start()
thread = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
thread.start()
thread.join()
finish = time()
print(finish - start)
