"""
Your job is to write a function which increments a string, to create a new string.
    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
Attention: If the number has leading zeros the amount of digits should be considered.

Если в конце стр, то прибавляем цифровую 1.

Если в конце инт, то:
Идти посимвольно с конца, проверяя каждый символ на int. 
Если символ str, засекаем индекс. Вычленяем цифровую часть.
Прибавляем к цифоровой части 1, конкатенируем со стр

try:
    x += 1
except TypeError:
    ...

>>> try:
...     int(y)+1
... except ValueError:
...     print ("last char is a letter")
...
"""

def string_incrementer(line):
    # last_char = line[-1:]
    separator = 0
    print("line is {}".format(line))

     
    for i in range(1, len(line)):
        try:
            separator += 1
            int(line[-i-1:-i])
            
            print("separator = {}".format(separator))
            # print("part_int = {}".format(line[-i-1:]))
            # print("part_str = {}".format(line[:-i-1]))
        except ValueError:
            break
    try:
        part_int = int(line[-separator:])
    except ValueError:
        return line + str(1)
    # part_str = line[:-separator]
    if separator == 0:
        part_int = 0
    part_str = line[:-len(str(part_int))]
    print("part_int = {}".format(part_int))
    print("part_str = {}".format(part_str))
    return part_str + str(int(part_int) + 1)
    
    # try:
    #     result = int(last_char) + 1
    # except ValueError:
    #     result = string_line + "1"
    # return result

# print(string_incrementer("foo"))
# print(string_incrementer("foobar23"))
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
print(string_incrementer("foo0042"))
# print(string_incrementer("foo9"))
print(string_incrementer("foo099"))