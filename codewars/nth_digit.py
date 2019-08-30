"""
Complete the function that takes two numbers as input, num and nth and return the nth digit of num 
(counting from right to left).

    If num is negative, ignore its sign and treat it as a positive value
    If nth is not positive, return -1
    Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0

findDigit(5673, 4)     returns 5
findDigit(129, 2)      returns 2
findDigit(-2825, 3)    returns 8
findDigit(-456, 4)     returns 0
findDigit(0, 20)       returns 0
findDigit(65, 0)       returns -1
findDigit(24, -8)      returns -1
"""

def find_digit(num, nth):
    if nth <= 0:
        return nth
    letters = list(str(abs(num)))
    return int(letters[len(letters) - nth])

print (find_digit(5673, 4))
print (find_digit(129, 2))
print (find_digit(-2825, 3))
print (find_digit(-456, 4))
print (find_digit(0, 20))
print (find_digit(65, 0))
print (find_digit(24, -8))