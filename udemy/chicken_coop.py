class Chicken:
    
    total_eggs = 0
    
    def __init__(self, species, name):
        self.name = name
        self.species = species
        self.eggs = 0
        
    def lay_egg(self):
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs

c1 = Chicken('Partridge Silkie', 'Molly')
c2 = Chicken('Specked Sussex', 'Whitie')

print(Chicken.total_eggs)
c1.lay_egg()
print(Chicken.total_eggs)
c2.lay_egg()
c2.lay_egg()
print(Chicken.total_eggs)
