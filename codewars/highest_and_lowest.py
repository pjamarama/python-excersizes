def high_and_low(numbers):
    int_num = [int(x) for x in numbers.split(' ')]
    return f'{max(int_num)} {min(int_num)}'

print(high_and_low('42'))