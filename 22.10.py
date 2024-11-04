# 0, 1, 1, 2, 3, 5, 8, 13, 21
a = 7
fibo_p, fibo_n = 0, 1
for _ in range(0, a):
    fibo_p, fibo_n = fibo_n, fibo_p + fibo_n
print(f'{a}-e число = {fibo_n}')


def func(a=7, fibo_p=0, fibo_n=1):
    if a == 0:
        return fibo_n
    return func(a - 1, fibo_n, fibo_p + fibo_n)


"""
func(a=7, fibo_p=0, fibo_n=1):
   func(a=6, fibo_p=1, fibo_n=0 + 1)
          func(a=5, fibo_p=1, fibo_n=1 + 1)
               func(a=4, fibo_p=2, fibo_n= 3)
                    func(a=3, fibo_p=3, fibo_n=5)
                         func(a=2, fibo_p=5, fibo_n=8)
                              func(a=1, fibo_p=8, fibo_n=13)
                                   func(a=0, fibo_p=13, fibo_n=21)

"""


def func_():
    return


print(func_())
func = lambda a, b: a + b
print(func(2,3))
print((lambda a, b: a + b)(2, 3))
