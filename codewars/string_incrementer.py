"""
v0.2
'beginning to end' approach

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
Attention: If the number has leading zeros the amount of digits should be considered.

>>> try:
...     int(y)+1
... except ValueError:
...     print ("last char is a letter")
"""

def string_incrementer(line):
    separator = 0
    print("line is {}".format(line))
     
    for i in range(len(line)):
        try:
            # type(int(line[i:i+1]) == int
            a = int(line[i:i+1]) + 1
            break
        except ValueError:
            separator += 1

    if separator == len(line):
        return line + "1"
    part_int = int(line[separator:]) # makes 42 from "0042"
    part_str = line[:-len(str(part_int))]
    return part_str + str (part_int+1)



    # try:
    #     part_int = int(line[-separator:])
    # except ValueError:
    #     return line + str(1)
    # # part_str = line[:-separator]
    # if separator == 0:
    #     part_int = 0
    # part_str = line[:-len(str(part_int))]
    # print("part_int = {}".format(part_int))
    # print("part_str = {}".format(part_str))
    # return part_str + str(int(part_int) + 1)
    

print(string_incrementer("foo"))
# print(string_incrementer("foobar23"))
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
print(string_incrementer("foo0042"))
print(string_incrementer("foo9"))
print(string_incrementer("foo099"))