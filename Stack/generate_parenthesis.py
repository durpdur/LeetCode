def generateParenthesis(n):
    # only add open paranthesis if open < n
    # only add a closing parathesis if close < open
    # valid IIF open == close == n
    
    stack = [] # hold paranthesis
    res = []   # holds list of valid paranthesis combinations
    
    def backtrack(openN, closedN):
        # when openN and closedN is equal to n, the solution is complete, so we store it in res
        if openN == closedN == n:
            res.append("".join(stack)) # joins current stack solution and puts it in res 
            return
        
        # when there has not yet been n open paranthesis, 
        if openN < n:
            stack.append("(") # slap a open parenthesis in the stack
            backtrack(openN + 1, closedN) # proceeds the path this combo will create
            stack.pop() # the part I don't understand is here
         
        if closedN < openN:
            stack.append(")") # slap a closed parenthesis int the stack
            backtrack(openN, closedN + 1)
            stack.pop()
    
    backtrack(0,0) # starts the backtrack recursive loop with openN and closedN set to 0
    return res

print(generateParenthesis(2))