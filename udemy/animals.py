voices = {
	'pig': 'oink',
	'dog': 'woof',
	'duck': 'quack',
	'cat': 'meow',
}

'''
def speak(animal='dog'):
	voice = voices.get(animal)
	if voice:
		return voice
	return '?'
'''


def speak (animal='dog'):
	return voices.get(animal, '?')
	
print(speak('pig'))
print(speak('duck'))
print(speak())
print(speak('roach'))
