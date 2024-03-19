# Table of Contents

1. [Arrays & Hashing](#a&h)

2. [Two Pointers](#twoPointers)
3. [Stack](#stack)

4. [Binary Search](#binarySearch)
5. [Sliding Window](#slidingWindow)
6. [Linked List](#linkedList)

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



## Arrays & Hashing <a name="a&h"></a>

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
- (first **n**)Check if the sum of the values in the map is 0

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


## Two Pointers <a name="twoPointers"></a>

- Currently Empty

## Stack <a name="stack"></a>

- Currently Empty

## Binary Search <a name="binarySearch"></a>

- Currently Empty

## Sliding Window <a name="slidingWindow"></a>

- Currently Empty

## Linked List <a name="Linked List"></a>

- Currently Empty

## Trees <a name="trees"></a>

- Currently Empty




