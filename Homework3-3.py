def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c = [1,2,3])

value_list = [3254324564, 324.234 , 'ttrtrt']
value_dict = {'a': 1231, 'b': True, 'c': 34534.234}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = ['sdfs', 231]
print_params(*value_list_2, 423)