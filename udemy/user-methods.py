# A User class with both instance attributes and instance methods
class User:
	active_users = 0
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	@classmethod
	def display_active_users(cls):
		return 'There are currently {} active users'.format(cls.active_users)

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(',')
		return cls(first, last, int(age))

	def logout(self):
		User.active_users -= 1
		return '{} has logged out'.format(self.first)

	def full_name(self):
		return "{} {}".format(self.first, self.last)

	def initials(self):
		return "{[0]}.{[0]}.".format(self.first, self.last)

	def likes(self, thing):
		return "{} likes {}".format(self.first, thing)

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return "Happy {}th, {}".format(self.age, self.first)

class Moderator(User):
	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1
	@classmethod
	def display_active_mods(cls):
		return 'There are currently {} active moderators'.format(cls.total_mods)

	def remove_post(self):
		return '{} removed a post from the {}'.format(self.full_name(), self.community)



print(User.display_active_users())
print(Moderator.display_active_mods())
u1 = User("Joe", "Smith", 68)
print(u1.full_name())
print(User.display_active_users())
print(Moderator.display_active_mods())
jasmine = Moderator('Jasmine', "O'connor", '62', 'Piano')
print(jasmine.full_name())
print(User.display_active_users())
print(Moderator.display_active_mods())

# user2 = User("Blanca", "Lopez", 41)



# print(jasmine.full_name())
# print(jasmine.community)

#
# print(user1.likes("Ice Cream"))
# print(user2.likes("Chips"))
#
# print(user2.initials())
# print(user1.initials())
#
# print(user2.is_senior())
# print(user1.age) #Print age before we update it
# print(user1.birthday()) #updates age
# print(user1.age) #Print new value of age
