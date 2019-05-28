def truncate(sentence, n):
    ts = sentence[:n]
    if n < 3:
        return "Truncation must be at least 3 characters."
    elif n > len(sentence):
        return sentence
    return ts.replace(ts[-3:], '...')


print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate('Aha', 3))
print(truncate("Yo",100))
# print(truncate())
# print(truncate())
# print(truncate())

'''
def find_factors(number):
    return [i for i in range(1, number+1) if number%i == 0]
'''