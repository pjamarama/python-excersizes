from functools import wraps
from time import sleep


def delay(timer):
    def inner(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            print('Waiting {}s before running {}'.format(timer, fn.__name__))
            sleep(timer)
            return fn(*args, **kwargs)
        return decorator
    return inner

@delay(4)
def say_hi():
    return 'hi'


print(say_hi())