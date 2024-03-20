def evalRPN(tokens):
    stack = []
    
    for t in tokens:
        if t == "+":
            a, b = stack.pop(), stack.pop()
            print(f"{a} + {b}")
            stack.append(a + b)
        elif t == "-":
            a, b = stack.pop(), stack.pop()
            print(f"{b} - {a}")
            stack.append(b - a)
        elif t == "*":
            a, b = stack.pop(), stack.pop()
            print(f"{a} * {b}")
            stack.append(a * b)
        elif t == "/":
            a, b = stack.pop(), stack.pop()
            print(f"{b} / {a}")
            stack.append(int(b / a))
        else:
            stack.append(int(t))
            
    return stack[0]
                
            
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(f"Result: {evalRPN(tokens)}")
