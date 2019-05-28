'''

'''

def find_greater_numbers(li):
    counter = 0
    for i in range(1, len(li)): 
        for k in range(0, i):
            if li[i] > li[k]:
                counter += 1
    return counter

print(find_greater_numbers([1,2,3])) # 3 
print(find_greater_numbers([6,1,2,7])) # 4
print(find_greater_numbers([5,4,3,2,1])) # 0
print(find_greater_numbers([])) # 0