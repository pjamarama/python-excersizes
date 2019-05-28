from copy import copy
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def __repr__(self):
        return ('Human named {} {}, age {}'.format(self.first, \
        self.last, self.age))
    def __len__(self):
        return self.age
    def __add__(self, other):
        if isinstance(other, Human):
            return Human('Newborn', last=self.last, age=0)
        raise TypeError ('It works only with ')
    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError ('You need to multiply by integer')

j = Human('Jenny', 'Larsen', 47)
k = Human('Kevin', 'Jones', 41)

# triplets = j * 3
# triplets[1].first = 'Jessica'
# triplets[0].first = 'Micheal'
# print(triplets)

triplets = (k + j) * 3
print(triplets)
