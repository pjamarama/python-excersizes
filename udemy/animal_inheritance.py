class Animal:
    def __init__(self, name, species):
    	self.name = name
    	self.species = species

    def __repr__(self):
    	return f'{self.name} is a {self.species}'

    def make_sound(self, sound):
        print(f'This animal says {sound}')

class Cat(Animal):
    def __init__(self, name, breed, toy):
    	super().__init__(name, species='Cat')
    	self.breed = breed
    	self.toy = toy

    def play(self):
    	return f'{self.name} plays with {self.toy}'

guinness = Cat('Guinness', 'No breed', 'tennis ball')

print(guinness.species)
print(guinness.breed)
print(guinness.toy)
guinness.make_sound('Hiss!')