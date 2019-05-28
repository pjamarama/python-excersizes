'''
Dictionary comprehensions
{___:___ for ___ in ___}

numbers = dict(first=1, second=2, third=3, fourth=4)
print ({k:v**3 for k,v in numbers.items()})

numlist = range(1, 6)
print ({num:num**3 for num in numlist})

str1 = 'ABCDE'
str2 = '12345'
print ({str1[i]:str2[i] for i in range(0, len(str1))})

Conditions:
numlist = range(1, 6)
print ({num:('even' if num % 2 == 0 else 'odd') for num in numlist})

loudsongname = {k:(v.upper() if k == 'songname' else v) for k,v in songrecord.items()}
'''
 
region_code = [38, 16, 177, 74, 66]
region_name = ['Irkutsk', 'Tatarstan', 'Moscow', 'Chelyabinsk', 'Sverdlovsk']

print({region_code[i]:region_name[i] for i in range(len(region_code))})
 
 
'''
songrecord = {
    'artist':'Jennifer Paige',
	'songname':'Crush',
	'albumname':'The Best',
	'songlength':'200'
}

loudrecord = {k:v.upper() for k,v in songrecord.items()}
loudsongname = {k:(v.upper() if k == 'songname' else v) for k,v in songrecord.items()}

print(loudrecord)
print(loudsongname)
'''





