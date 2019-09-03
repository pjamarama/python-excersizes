class Mother:
    def __init__(self):
        self.eyecolor = 'brown'
        self.hair_color = 'dark brown'
        self.hair_type = 'curly'



class Father:
    def __init__(self):
        self.eyecolor = 'blue'
        self.hair_color = 'blond'
        self.hair_type = 'straight'


class Child(Mother, Father):
    def __init__(self, eyecolor, hair_color, hair_type):
        super().__init__(self)
        self.eyecolor = eyecolor
        self.hair_color = hair_color
        self.hair_type = hair_type

tammy = Mother()

bob = Father()


jake = Child()
print(jake.eyecolor())