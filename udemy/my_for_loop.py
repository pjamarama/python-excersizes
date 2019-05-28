def my_for(word):
    it = iter(word)
    while True:
        try:
            print(next(it))
        except StopIteration:
            print('End of iterator')
            break

my_for('Dzheltz')
