class Human:
    def __init__(self, height):
        self.height = height
    def __len__(self):
        return self.height

alex = Human(168)
print(len(alex))