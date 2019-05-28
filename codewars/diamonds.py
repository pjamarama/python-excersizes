'''
expected =  " *\n"
expected += "***\n"
expected += " *\n"
test.assert_equals(diamond(3), expected)

The shape that will be returned from print method resembles a diamond, 
where the number provided as input represents the number of *’s printed 
on the middle line. The line above and below will be centered and will 
have 2 less *’s than the middle line. This reduction by 2 *’s for each 
line continues until a line with a single * is printed at the top and 
bottom of the figure.

Return null if input is even number or negative (as it is not possible 
to print diamond with even number or negative number).
'''

def diamond(n):
    d1 = '*\n'
    d2 = 

    return pass