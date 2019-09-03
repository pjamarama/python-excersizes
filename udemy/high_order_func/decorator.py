def be_polite(fn):
    def wrapper():
        print('Pleasure to meet you!')
        fn()
        print('Have a nice day!')
    return wrapper

def greet():
    print('My name is Alex')



g = be_polite(greet)

g()

