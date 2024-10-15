import random

def gates():
    numbers = [3, 4 ,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    n = random.choice(numbers)
    numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    key = [n, ' ']
    while n in numbers[0: 18]:
        for i in numbers_[0: 20]:
            for j in numbers_[i - 1: 20]:
                if i == j:
                    continue
                elif n % (i + j) == 0:
                    key.extend([i, j])
                else:
                    continue
        numbers.remove(n)
    return key
key = ''.join(str(item) for item in gates())
print(key)

