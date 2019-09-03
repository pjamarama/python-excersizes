class User:

    acitve_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.acitve_users += 1

    def __repr__(self):
        return f'{self.first} is {self.age}'

    def logout(self):
        User.acitve_users -= 1
        return f'{self.first} has left'

    def full_name(self):
        return f'{self.first} {self.last}'

    def initials(self):
        return f'{self.first[0]}.{self.last[0]}.'

    def likes(self, thing):
        return f'{self.first} likes {thing}'

    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th birthday, {self.first}'

    def is_senior(self):
        return self.age >= 65

    @classmethod
    def display_active_users(cls):
        return f'There are {cls.acitve_users} \
active users'

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(',')
        return cls(first, last, int(age))



# print(User.display_active_users())
# user1 = User('Alex', 'Grokhotov', 35)
# user2 = User('Eve', 'Mendez', 38)
# print(User.display_active_users())

# print(user2.first, user1.last, user2.age)
# print(user1.likes('Ice Cream'))
# print(user2.likes('Coke'))

# print(user1.initials())

# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

tom = User.from_string('Tom,Jones,63')
print(tom)

e = User('Eve', 'Mendez', 38)
print(e)