"""
https://www.codewars.com/kata/576757b1df89ecf5bd00073b
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
"""

def build(n_floors):
    x = 2 * n_floors - 1 # amount of symbols in the string (floor)
    floors = []

    for i in range(n_floors):
        l_stars = 2 * i + 1 # lengh of '*' part
        l_spaces = (x - 1) // 2 - i # length of ' ' part
        floor = l_spaces * ' ' + '*' * l_stars + l_spaces * ' '
        floors.append(floor)

    # for floor in floors:
    #     print(floor)
    return floors


print(build(3))




    
