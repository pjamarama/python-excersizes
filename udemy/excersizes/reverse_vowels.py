'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''

def reverse_vowels(word):
    vowels = 'aeiou'
    word = list(word)
    # define an i-index to start from the beginning
    i = 0
    # define an j-index to start from the end
    j = len(word)-1
    
    #define the loop
    while i < j:
    # if the i is not a vowel, move on
        if word[i].lower() not in vowels:
            i += 1
        # if the j is not a vowel, move on
        elif word[j].lower() not in vowels:
            j -= 1
        # if i and j are vowels, swap them
        else:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

    return ''.join(word)


print(reverse_vowels("Hello!"))
print(reverse_vowels("Tomatoes"))
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))
print(reverse_vowels("why try, shy fly?"))










'''
def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)
'''