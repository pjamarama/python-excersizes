'''
Instructions

Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of 
all capital letters in the string.
Example

Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
'''

# def capitals(word):
#     caplist = []
#     for letter in word:
#         if 64 < ord(letter) < 91:
#             caplist.append(word.index(letter))
#     return caplist

# def capitals(word):
#     return [word.index(letter) for letter in word if 64 < ord(letter) < 91]


# def capitals(word):
#     caplist = []
#     for count in range(len(word)):
#         if 64 < ord(word[count]) < 91:
#             caplist.append(count)
#     return caplist

def capitals(word):
    return [count for count in range(len(word)) if 64 < ord(word[count]) < 91]


print(capitals('CodEWaRs'))
print(capitals('IwillSurViVE'))

