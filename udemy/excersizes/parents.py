'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False

    def valid_parentheses(parens):
        count = 0
        i = 0
        while i < len(parens):
            if (parens[i] == '('):
                count += 1
            if (parens[i] == ')'):
                count -= 1
            if (count < 0):
                return False
            i += 1
        return count == 0

'''




def valid_parentheses(sample):
    count = 0
    i = 0
    while i < len(sample):
        if sample[i] == '(':
            count +=1 
        if sample[i] == ')':
            count -= 1
        if count < 0:
            return False
        i += 1
    return count == 0





#     if sample.count('(') == sample.count(')'):
#         return True
#     return False

print(valid_parentheses("()")) # True 
print(valid_parentheses(")(()))")) # False 
print(valid_parentheses("(")) # False 
print(valid_parentheses("(())((()())())")) # True 
print(valid_parentheses('))((')) # False
print(valid_parentheses('())(')) # False
print(valid_parentheses('()()()()())()(')) # False

    