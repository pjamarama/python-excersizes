"""
Complete the function to return true if the two arguments given are anagrams of the each other; 
return false otherwise.

create a list of 'original' letters
select the letter from 'test' one by one and .remove(letter)
if ValueError appears, return false
if len(list) != 0 when all 'test' letters are gone, return false
return true

Codewars solution:
return sorted(original.lower()) == sorted(test.lower()) 

"""

def is_anagram(test, original):
    orig_list = list(original.lower())
    for letter in test.lower():
        try:
            orig_list.remove(letter)
        except ValueError:
            return False
    if len(orig_list) != 0:
        return False
    return True

print(is_anagram("foefet", "toffee"))
        
    