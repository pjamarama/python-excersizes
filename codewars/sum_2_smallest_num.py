def sum_two_smallest_numbers(numbers):
    '''
	s1 = numbers.index(min(numbers))
    r1 = numbers.pop(s1)
    s2 = numbers.index(min(numbers))
    r2 = numbers.pop(s2)
    return r1 + r2
'''
    return sum(sorted(numbers)[0:2])

print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
