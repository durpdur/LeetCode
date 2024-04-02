class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures) # holds the result
        stack = [] # holds the stack
        
        for tempIndex in range(len(temperatures)): # for all elements in temp, and the index being kept track of by tempIndex
            while stack and temperatures[tempIndex] > temperatures[stack[-1]]: # while the stack is not empty and the top of the stack is smaller than the temp
                                                                            # or think of it as if the stack is empty or if the top of stack is bigger than the temp
                index = stack.pop() # keep popping until the top of stack is smaller than temp, or the stack is empty
                res[index] = tempIndex - index # keep updating the res[index] with the difference
            stack.append(tempIndex) 
            
        return res
                
    
solution = Solution()
array = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(array))