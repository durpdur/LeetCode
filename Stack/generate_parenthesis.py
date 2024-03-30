import os
import sys 

os.system("clear")
def print_error(message):
    sys.stderr.write("\033[91m{}\033[0m\n".format(message))

def generateParenthesis(n):
    # only add open paranthesis if open < n
    # only add a closing parathesis if close < open
    # valid IIF open == close == n
    
    stack = [] # hold paranthesis
    res = []   # holds list of valid paranthesis combinations
    
    def backtrack(openN, closedN):
        # when openN and closedN is equal to n, the solution is complete, so we store it in res
        if openN == closedN == n:
            print(f"backtrack({openN}, {closedN})")
            print_error(f"Ending reached:     {stack}\n")
            res.append("".join(stack)) # joins current stack solution and puts it in res 
            return
        
        # when there has not yet been n open paranthesis, 
        if openN < n:
            stack.append("(")
            print(f"backtrack({openN}, {closedN})")
            print(f"if openN < n:       {stack}\n")
            backtrack(openN + 1, closedN) # proceeds the path this combo will create
            print_error(f"Pop!: {stack.pop()}") # goes back to the last backtrack call in the stack before popping
        
        if closedN < openN:
            stack.append(")") # slap a closed parenthesis in the stack
            print(f"backtrack({openN}, {closedN})")
            print(f"if closedN < openN: {stack}\n")
            backtrack(openN, closedN + 1)
            print_error(f"Pop!: {stack.pop()}")
            
    backtrack(0,0) # starts the backtrack recursive loop with openN and closedN set to 0
    return res

print(generateParenthesis(3))