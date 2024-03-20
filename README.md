# Just some good ol' NeetCode to fry the brain

# Table of Contents

1. [Arrays & Hashing](#arrays--hashing)

2. [Two Pointers](#two-pointers)
3. [Stack](#stack)

4. [Binary Search](#binary-search)
5. [Sliding Window](#sliding-window)
6. [Linked List](#linked-list)

7. [Trees](#trees)

8. [Tries]
9. [Backtracking]

10. [Heap / Priority Queue]

11. [Graphs]
12. [1-D DP]

13. [Intervals]
14. [Greedy]
15. [Advanced Graphs]
16. [2-D DP]
17. [Bit Manipulation]

18. [Math & Geometry]

# Arrays & Hashing

1. [Contains Duplicate]
2. [Valid Anagram](#242-valid-anagram)
3. [Two Sum]
4. [Group Anagrams]
5. [Top K Frequent Elements]
6. [Product of Array Except Self]
7. [Valid Sudoku]
8. [Encode and Decode Strings]
9. [Longest Consecutive Sequence]

## 242. Valid Anagram

### Solution 1:

Time Complexity: $O(n)$
Explanation:

- Check if length of first string is equal to second string
- Create a map of size 26
- (first **n**) Iterate through both strings at the same time
  - At the index of the letter
    - increase the value for the first string
    - decrease the value for the second string
- (first **n**) Check if the sum of the values in the map is 0

```python
class Solution(object):
	def isAnagram(self, s, t):
		if len(s) != len(t):
			return False

		# an array of size 26 is created
		char_count_array = [0] * 26

		# iterating through both string with a counter
		for i in range(len(s)):
			# ord(s[i]) - ord('a') just gives you the appropriate index
			# 'a' is the baseline first value of the character
			# s[i] is the character you are targetting
			char_count_array[ord(s[i]) - ord('a')] += 1
			char_count_array[ord(t[i]) - ord('a')] -= 1

		# loop through all values in to check if there is anything other than 0
		for count in char_count_array:
			if count != 0:
				return False
		return True
```

# Two Pointers

- Currently Empty

# Stack

1. [Valid Parenthesis]
2. [Min Stack](#155-min-stack)
3. [Evaluate Reverse Polish Notation]
4. [Generate Parentheses]
5. [Daily Temperatures]
6. [Car Fleet]
7. [Largest Rectangle In Histogram]

## 155. Min Stack

### Prompt:

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with `O(1)` time complexity for each function.

### Solution 1:

#### Explanation:

##### `def __init__(self):`

- To Initialize the MinStack object, we first need two stacks
  - `stack` for the original stack
  - `minStack` for keeping track of the smallest item whenever a new item is added

##### `def push(self, val):`

- `push()`'s goal is to push something to the top of `stack`
  - `stack` can just be appended
  - the **_min value_** in the current stack needs to be appended to `minStack`
    - if `self.minStack` has something in it:
      - the smaller of (value being appended, and the top of minStack(representing the current smallest value)) gets appended
    - if not:
      - just append the value
  - Now every time when `stack` gets popped, the min value for that the state `stack` is in gets matched

##### `def pop(self):`

- With `minStack` keeping track of the state of the smallest value in `stack`
  - we can just pop off both `stack` and `minStack`

##### `def top(self):`

- `top()` just returns the top of the stack
  - so `return self.stack[-1]`

##### `def getMin(self):`

- we want `getMin()` to return the current smallest value
- `minStack` is keeping track of the smallest value
- `return self.minStack[-1]`

```Python
class MinStack(object):
	def __init__(self):
		self.stack = []
		self.minStack = []

	def push(self, val):
		self.stack.append(val)
		if self.minStack:
			val = min(val, self.minStack[-1])
		else:
			val = val
		self.minStack.append(val)

	def pop(self):
		self.stack.pop()
		self.minStack.pop()

	def top(self):
		return self.stack[-1]

	def getMin(self):
		return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

# Binary Search

- Currently Empty

# Sliding Window

- Currently Empty

# Linked List

- Currently Empty

# Trees

- Currently Empty
