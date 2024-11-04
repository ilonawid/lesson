data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]



def calculate_structure_sum():
    list_ = []
    for i in data_structure:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, str):
                    list_.append(int(len(j)))

        elif isinstance(i, tuple):
            for j in i:
                if isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, str):
                    list_.append(int(len(j)))
        elif isinstance(i, dict):
            list_for_dict = i.items()
            for j in list_for_dict:
                for a in j:
                    if isinstance(a, int):
                        list_.append(a)
                    elif isinstance(a, str):
                        list_.append(int(len(a)))
        elif isinstance(i, set):
            for j in i:
                if isinstance(j, int):
                    list_.append(j)
                elif isinstance(j, str):
                    list_.append(int(len(j)))
        elif isinstance(i, int):
            list_.append(i)
        elif isinstance(i, str):
            list_.append(int(len(i)))
    sum_ = sum(list_)
    return sum_


result = calculate_structure_sum()

print(result)
