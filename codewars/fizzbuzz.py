'''
Напишите программу, которая выводит цифры от 1 до 100. 
Но для чисел, кратных трем, нужно выводить Fizz вместо 
самой цифры, а для чисел, кратных пяти, Buzz. Для чисел, 
которые кратны и трем, и пяти, выводите на экран слово 
FizzBuzz.
'''

for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
