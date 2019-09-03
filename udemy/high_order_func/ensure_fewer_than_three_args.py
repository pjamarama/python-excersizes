'''
@ensure_fewer_than_three_args
    def add_all(*nums):
        return sum(nums)

    add_all() # 0
    add_all(1) # 1
    add_all(1,2) # 3
    add_all(1,2,3) # "Too many arguments!"
    add_all(1,2,3,4,5,6) # "Too many arguments!"
'''

from functools import wraps

def ensure_fewer_than_three_args(fn):
    @wraps(fn)
    def wrapper(*args):
        if len(args) > 2:
            return print("Too many arguments!")
        return fn(*args)
    return wrapper

@ensure_fewer_than_three_args
def add_all(*nums):
    return print(sum(nums))

add_all() # 0
add_all(1) # 1
add_all(1,2) # 3
add_all(1,2,3) # "Too many arguments!"
add_all(1,2,3,4,5,6) # "Too many arguments!"
