data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

list_ = []


def calculate_structure_sum():
    for i in data_structure:
        type_ = type(i)

    def f_list():
        if isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, str):
                    list_.append(int(len(j)))

    def f_tuple():
        if isinstance(i, tuple):
            for j in i:
                if isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, str):
                    list_.append(int(len(j)))
                elif isinstance(j, dict):
                    list_for_dict = j.items()
                    for k in list_for_dict:
                        for a in k:
                            if isinstance(a, int):
                                list_.append(a)
                            elif isinstance(a, str):
                                list_.append(int(len(a)))
                elif isinstance(j, list):
                    for k in j:
                        if isinstance(k, int):
                            list_.append(k)
                        elif isinstance(k, str):
                            list_.append(int(len(k)))
                        elif isinstance(k, set):
                            for a in k:
                                if isinstance(a, int):
                                    list_.append(a)
                                elif isinstance(a, str):
                                    list_.append(int(len(a)))
                                elif isinstance(a, tuple):
                                    for m in a:
                                        if isinstance(m, int):
                                            list_.append(m)
                                        elif isinstance(m, str):
                                            list_.append(int(len(m)))
                                        elif isinstance(m, tuple):
                                            for n in m:
                                                if isinstance(n, int):
                                                    list_.append(n)
                                                elif isinstance(n, str):
                                                    list_.append(int(len(n)))

    def f_dict(*args):
        if isinstance(i, dict):
            list_for_dict = i.items()
            for j in list_for_dict:
                for a in j:
                    if isinstance(a, int):
                        list_.append(a)
                    elif isinstance(a, str):
                        list_.append(int(len(a)))

    def f_set():
        # if isinstance(i, set):
        for j in i:
            if isinstance(j, int):
                list_.append(j)
            elif isinstance(j, str):
                list_.append(int(len(j)))

    def f_int():
        # if isinstance(i, int):
        list_.append(i)

    def f_str():
        # if isinstance(i, str):
        list_.append(int(len(i)))

    for i in data_structure:
        if isinstance(i, list):
            f_list()
        elif isinstance(i, tuple):
            f_tuple()
        elif isinstance(i, dict):
            f_dict()
        elif isinstance(i, set):
            f_set()
        elif isinstance(i, int):
            f_int()
        elif isinstance(i, str):
            f_str()
    sum_ = sum(list_)
    return sum_


print(calculate_structure_sum())
