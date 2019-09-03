from random import choice

def make_laugh_at_func(name):
    def get_laugh():
        laugh = choice(('Mwa-ha-ha!', 'tehehe', 'Hah-hah!'))
        return f'{laugh} {name}'
    return get_laugh()

print(make_laugh_at_func('Linda'))
print(make_laugh_at_func('Linda'))
print(make_laugh_at_func('Linda'))
print(make_laugh_at_func('Linda'))
print(make_laugh_at_func('Linda'))
print(make_laugh_at_func('Linda'))