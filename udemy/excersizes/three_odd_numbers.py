'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(li):
    for i in range(len(li)-2):
        if sum(li[i:i+3])%2 != 0:
            return True
    return False




print(three_odd_numbers([1,2,3,4,5]))
print(three_odd_numbers([0,-2,4,1,9,12,4,1,0]))
print(three_odd_numbers([5,2,1]))
print(three_odd_numbers([1,2,3,3,2]))