class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] <= t:
                topIndex = stack.pop()
                res[topIndex] = i - topIndex
            stack.append(i)
            
        return res
            
                
    
solution = Solution()
array = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(array))

'''
1. we are going through every element in the list
2. when we hit a larger element, we want something to happen
3. In this case, we want to use monotonic stack
4. the monostatic stack be strictly decreasing
5. 73 pop 74 pop 75 71 69 pop pop 72
'''