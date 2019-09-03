def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

c = count_up_to(5)

for num in c:
    print(num)
