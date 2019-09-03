'''
Your task is to make a function that can take any 
non-negative integer as a argument and return it 
with its digits in descending order. Essentially, 
rearrange the digits to create the highest possible 
number.
'''

def descending(number):
    slistik = sorted([n for n in str(number)], reverse=True)
    dslistik = ''
    for i in range(len(slistik)):
        dslistik += slistik[i]
    return int(dslistik)

print(descending(235314))
