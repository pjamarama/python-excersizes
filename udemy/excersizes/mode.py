'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

def mode(collection):    
    frequency = 0
    most_freq_element = 0
    for i in collection:
        if collection.count(i) > frequency:
            frequency = collection.count(i)
            most_freq_element = i
    return most_freq_element


# create a dictionary collection
# find max frequency
# find at which index max freq is
# return the key from the list of a dict at this index


# def mode(li):    
#     di = {x:li.count(x) for x in li}
#     max_count = max(di.values())
#     correct_index = list(di.values()).index(max_count)
#     return list(di.keys())[correct_index]

print(mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))
print(mode('tyronasaurus rex'))