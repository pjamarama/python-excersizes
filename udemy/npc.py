class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level
    
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(self, name ,hp, level)
        
    
    @classmethod
    def speak(cls):
        return ('{} says: I heard there were monsters \
running around last night!'.format(cls.name))

aragorna = Character('Aragorna', 34, 1)

healer = NPC('Tuck', 61, 20)
print(healer.speak())

'''

'''