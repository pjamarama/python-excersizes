class GrumpyDict(dict):
    def __repr__(self):
        print('None of your business!')
        return super().__repr__()
    def __missing__(self, key):
        return 'You want "{}"? Well, it ain\'t here!'.format(key)

data = GrumpyDict({'name': 'Tom', 'animal': 'cat'})
print(data)
print(data['last'])
