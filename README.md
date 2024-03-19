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
#### Solution 1:
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

- Currently Empty

# Binary Search

- Currently Empty

# Sliding Window

- Currently Empty

# Linked List

- Currently Empty

# Trees

- Currently Empty




