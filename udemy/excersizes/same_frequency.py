'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(n1, n2):
    # n1_dict = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    # n2_dict= {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    # for d in str(n1):
    #     if d in str(n1):
    #         n1_dict[d] += 1
    # for d in str(n2):
    #     if d in str(n2):
    #         n2_dict[d] += 1

    # n1_dict = {digit:str(n1).count(digit) for digit in str(n1) if digit in str(n1)}
    # n2_dict = {digit:str(n2).count(digit) for digit in str(n2) if digit in str(n2)}
    if {digit:str(n1).count(digit) for digit in str(n1) if digit in str(n1)} == \
        {digit:str(n2).count(digit) for digit in str(n2) if digit in str(n2)}:
        return True
    return False

print(same_frequency(551122,221515)) # True
print(same_frequency(321142,3212215)) # False
print(same_frequency(1212, 2211)) # True

