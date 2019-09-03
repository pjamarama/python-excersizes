def fib_list(max):
    count = 1
    a, b = 0, 1
    while count < max:
        a, b = b, a + b
        yield b
        count += 1

fl = fib_list(15)
for n in fl:
    print(n)

