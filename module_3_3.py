def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

valius_list = (1, 'текст', True)
valius_dict = {'a': 5, 'b': False, 'c': 'формула'}
print_params(*valius_list)
print_params(**valius_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)