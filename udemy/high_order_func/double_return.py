def double_return(fn):
    def wrapper(*args, **kwargs):
        return [fn(*args, **kwargs), fn(*args, **kwargs)]
    return wrapper

@double_return
def ad(a,b):
    return a + b

@double_return
def greet(name):
    return "Hi, I'm " + name

print (ad(2, 3))
print (greet('Alex'))