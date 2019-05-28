'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(phrase):
    phl = phrase.split()
    result = []
    for word in phl:
        cw = word[0].upper() + word[1:]
        result.append(cw)
    print(result)
    return ' '.join(result)


print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))