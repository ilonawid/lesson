my_dict = {'Wine': 75, 'Mozzarella': 89, 'roll': 65}
print(my_dict)
my_dict['chocolate'] = 95
print(my_dict['Wine'])
print(my_dict['chocolate'])
my_dict.update({'ice_cream': 100,
                'cofee': 90})
print(my_dict)
a = my_dict.pop('Mozzarella')
print(a)
my_set = {1, 69, 37, True, 'Boo', 69, True}
print(my_set)
my_set.add(73)
my_set.add(False)
my_set.discard(1)
print(my_set)
