def beats():
    num = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(num): i = 0
        yield num[i]
        i += 1

