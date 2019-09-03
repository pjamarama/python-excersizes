'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

# def make_song(num, beverage):
#     count = num
#     while count >= 0:
#         if count == 1:
#             yield f'Only 1 bottle of {beverage} left!'
#             count -= 1
#         elif count == 0:
#             yield f'No more {beverage}'
#             count -= 1
#         else:
#             yield f'{count} bottles of {beverage} on the wall.'
#             count -= 1

# This one works too:
def make_song(num, beverage):
    while num >= 0:
        if num == 1:
            yield f'Only 1 bottle of {beverage} left!'
            num -= 1
        elif num == 0:
            yield f'No more {beverage}'
            num -= 1
        else:
            yield f'{num} bottles of {beverage} on the wall.'
            num -= 1

    def make_song(verses=99, beverage="soda"):
        for num in range(verses, -1, -1):
            if num > 1:
                yield "{} bottles of {} on the wall.".format(num, beverage)
            elif num == 1:
                yield "Only 1 bottle of {} left!".format(beverage)
            else:
                yield "No more {}!".format(beverage)


song = make_song(4, 'wine')