'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(collection, value, index=0):
    if type(collection) is dict:
        return value in collection.values()
    truncated_collection = collection[index:] 
    return value in truncated_collection

print(includes([1, 2, 3], 1))
print(includes([1, 2, 3], 1, 2))
print(includes({ 'a': 1, 'b': 2 }, 1))
print(includes({ 'a': 1, 'b': 2 }, 'a'))
print(includes('abcd', 'b'))
print(includes('abcd', 'e'))

    