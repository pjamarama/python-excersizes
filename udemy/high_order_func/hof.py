# def summa(n, func):
#     st = 0
#     for i in range (1, n+1):
#         st += func(i)
#     return st

# def square(m):
#     return m*m

# print(summa(3, square))



def sim(y, funkcia):
    result = 0 
    for i in range(1, y+1):
        result += funkcia(i)
    return result

def cube(k):
    return k*k*k

print(sim(5, cube))