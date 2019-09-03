from random import choice

# def greetings(name):
#     def mood():
#         ans = ('Hi ', 'I love you ', 'Go away ')
#         return choice(ans)
#     result = mood() + name
#     return result

def greetings(name):
    def mood():
#        ans = ('Hi ', 'I love you ', 'Go away ')
        return choice(('Hi ', 'I love you ', 'Go away '))
    return mood() + name

print(greetings('Toby'))