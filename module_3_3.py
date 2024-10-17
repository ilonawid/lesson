# 1
def print_params(a=22, b='Oxygen', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

# 2

values_list = [22, 'Oxygen', False]
values_dict = {'a': True, 'b': 'Nitrogen', 'c': 37}
print_params(*values_list)
print_params(**values_dict)

# 3

values_list_2 = [1828, True]
print_params(*values_list_2, 42)

# good day, sir:)
