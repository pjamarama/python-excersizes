'''
def get_middle(s):
    #your code here
    #s = input('Enter a s: ')
    n = len(s)
    if n % 2 == 0:
        return s[(n//2-1):(n//2+1)]
    return s[(n-1)//2]
'''



def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
   
   print(get_middle('sasa'))