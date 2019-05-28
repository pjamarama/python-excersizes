class Aquatic:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return '{} is swimming'.format(self.name)

    def greet(self):
        return 'I am {} of the sea!'.format(self.name)

class Ambulatory:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return '{} is walking'.format(self.name)

    def greet(self):
        return 'I am {} of the land!'.format(self.name)

class Penguin(Aquatic, Ambulatory):
    def __init__(self, name):
        super().__init__(name=name)

# jaws = Aquatic('Jaws')
# lassie = Ambulatory('Lassie')
captain_cook = Penguin('Captain Cook')

print(captain_cook.greet())
# print(isinstance(captain_cook, Penguin))
# print(isinstance(captain_cook, Ambulatory))
# print(isinstance(captain_cook, Aquatic))

print(Penguin.__mro__)
print(Penguin.mro())
help(Penguin)
