def isValid(s):
    bracketStack = []
    dictOfBracket = {
        '}' : '{',
        ']' : '[',
        ')' : '('
    }

    for c in s:
        # when we hit a closed bracket
        if c in dictOfBracket:
            print(c)
            # check if bracketStack is empty or not, 
            # great, its not empty, is the top of the stack the same?
            # it is? sick, pop it off and keep going
            # it isn't? sheee, return false
            if bracketStack and dictOfBracket[c] == bracketStack[-1]:
                bracketStack.pop()
            else:
                print(f"{c}First Check failed")
                return False
        else:
            #if it's not an open bracket it must be an open bracket
            bracketStack.append(c)
    
    if bracketStack:
        return False
    else:
        return True

s = "(){}[][({})]"    
print(isValid(s))