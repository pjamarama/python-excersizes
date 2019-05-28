
def range_in_list(listik, b=0, e=0):
    # print(b, e)
    if e == 0:
        return sum(listik[b:])
    return sum(listik[b:e+1])

print(range_in_list([1,2,3,4],0,2)) #  6
print(range_in_list([1,2,3,4],0,3)) # 10
print(range_in_list([1,2,3,4],1)) #  9
print(range_in_list([1,2,3,4])) # 10
print(range_in_list([1,2,3,4],0,100)) # 10
print(range_in_list([],0,1)) # 0
 