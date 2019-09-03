def get_multiples(number=1, count=10):
    next_number = number
    while count > 0:
        yield next_number
        next_number += number
        count -= 1

mul = get_multiples()
for n in mul:
    print (n)