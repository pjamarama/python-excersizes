from functools import wraps

def ensure_no_quargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError ('No kwargs allowed!')
        return fn(*args, **kwargs)
    return wrapper

@ensure_no_quargs
def greet(name):
    print('Hi there {}'.format(name))

# greet('Albert')

greet(name='John')