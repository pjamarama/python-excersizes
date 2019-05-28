'''
# {'a':'b'}
{}.fromkeys('a', 'b') 

#{'email':'unknown'}
{}.fromkeys(['email'], 'unknown')

#{'a':[1,2,3,4]}
{}.fromkeys('a', [1,2,3,4])
'''

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]


#dict comprehension
answer = {x[0]:x[1] for x in person}


#dict comprehension no indices
answer = {k:v for k,v in person}



#If you have a list of pairs, you can very easily turn it into a dictionary using dict()

answer = dict(person)