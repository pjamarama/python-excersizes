'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(keys, values):
    result = {}
    for index, value in enumerate(keys):
        if index < len(values):
            result[keys[index]] = values[index]
        else:
            result[keys[index]] = None
    return result


print(two_list_dictionary(['x', 'y', 'z']  , [1,2]))
