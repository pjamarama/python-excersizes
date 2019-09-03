from functools import wraps
from time import time

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'Executing {fn.__name__}')
        print(f'Time elapsed: {end_time - start_time}')
        return result
    return wrapper

@speed_test
def sum_nums(num):
    return sum(i for i in range (1,num))

@speed_test
def list_sum(num):
    return sum([i for i in range(1, num)])

print (sum_nums(10000000))
print(list_sum(10000000))