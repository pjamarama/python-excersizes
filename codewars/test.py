d ={}
for i in 'qwerty':
    d['{}'.format(i)] = i

print(d)

'''
>>> name = '/a/abbey/sun_aqswjsnjlrfzzhiz.jpg'
>>> name.split('/')
['', 'a', 'abbey', 'sun_aqswjsnjlrfzzhiz.jpg']
>>> name.split('/')[2]
'abbey'
'''