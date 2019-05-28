'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps

# def ensure_authorized(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         if kwargs != {"role":'admin'}:
#             return print('Unauthorized')
#         return fn(*args, **kwargs)
#     return wrapper

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # if kwargs.get('role') == 'admin':
        if kwargs == {'role':'admin'}:
            return fn(*args, **kwargs) 
        return print('Unauthorized')
    return wrapper

@ensure_authorized
def show_secrets(*args, **kwargs):
    return print("Shh! Don't tell anybody!")

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"

