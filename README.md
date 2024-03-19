# Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Introduction <a name="introduction"></a>

Brief introduction to your project goes here.

## Installation <a name="installation"></a>

Instructions on how to install your project.

## Usage <a name="usage"></a>

Examples and guidelines on how to use your project.

## Contributing <a name="contributing"></a>

Guidelines on how to contribute to the project.

## License <a name="license"></a>

Information about the project's license.



# 242. Valid Anagram
## Solution 1:
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
