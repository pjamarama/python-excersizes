class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            self._age = 0

jane = Human('Jane', 'Goodall', 62)

print(jane.get_age())
jane.set_age(50)
print(jane.get_age())