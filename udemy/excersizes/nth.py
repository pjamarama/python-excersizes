'''
nth(['a', 'b', 'c', 'd'], 1)  # 'b' 
nth(['a', 'b', 'c', 'd'], -2) #  'c'
nth(['a', 'b', 'c', 'd'], 0)  # 'a'
nth(['a', 'b', 'c', 'd'], -4) #  'a'
nth(['a', 'b', 'c', 'd'], -1) #  'd'
nth(['a', 'b', 'c', 'd'], 3)  # 'd'
'''

def nth(li, nu):
    if nu < 0:
        return li[len(li)+nu]
    return li[nu]

print(nth(['a', 'b', 'c', 'd'], 1))  # 'b' 
print(nth(['a', 'b', 'c', 'd'], -2)) #  'c'
print(nth(['a', 'b', 'c', 'd'], 0))  # 'a'
print(nth(['a', 'b', 'c', 'd'], -4)) #  'a'
print(nth(['a', 'b', 'c', 'd'], -1)) #  'd'
print(nth(['a', 'b', 'c', 'd'], 3))  # 'd'