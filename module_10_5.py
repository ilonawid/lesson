import multiprocessing
from datetime import datetime
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as name:
        while True:
            string = name.readline().strip()
            all_data.append(string)
            if not string:
                break

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = datetime.now()

for f in files:
    read_info(f)

end1 = datetime.now()
time_of_line_function = end1 - start1
print(f'Время работы линейного вызова : {time_of_line_function}')

if __name__ == '__main__':
    start2 = datetime.now()

    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)

    end2 = datetime.now()
    time_of_multiprocessing = end2 - start2
    print(f'Время работы мультипроцесса : {time_of_multiprocessing}')


