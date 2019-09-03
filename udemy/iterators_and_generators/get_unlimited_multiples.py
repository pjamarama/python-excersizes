def get_unlimited_multiples(num=1):
    count = 1
    while True:
        yield count * num
        count += 1

