# class Animal:
#     def speak(self):
#         raise NotImplementedError ('Only subclasses do that')

# class Dog(Animal):
#     def speak(self):
#         return 'woof-woof'

# class Cat(Animal):
#     def speak(self):
#         return 'meow-meow'

# class Wombat(Animal):
#     pass

# fido = Dog()
# print(fido.speak())

# jelly = Wombat()
# print(jelly.speak())

class Animal:
    def speak(self):
        # raise NotImplementedError('Only subclasses do that')
        return "wo-o, I'm an animal"

class Bird(Animal):
    def speak(self):
        return 'Tweet!'

class Horse(Animal):
    def speak(self):
        return 'Eego-go!'

class Fish(Animal):
    pass

amber = Horse()
lilly = Bird()
tush = Fish()

print(amber.speak())
print(lilly.speak())
print(tush.speak())