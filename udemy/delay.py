from functools import wraps
from time import sleep

# def delay(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print('Waiting 3s before running say_hi')
#         time.sleep(3)
#         fn()
#     return wrapper

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay
def say_hi():
    return print('hi')


say_hi()

