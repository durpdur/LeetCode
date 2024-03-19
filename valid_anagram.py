class ValidAnagram:
    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        
        char_count_array = [0] * 26
        
        for i in range(len(s)):
            char_count_array[ord(s[i]) - ord('a')] += 1
            char_count_array[ord(t[i]) - ord('a')] -= 1
            
        for count in char_count_array:
            if count != 0:
                return False
        return True
    
    def __init__(self) -> None:
        pass
    
valid_anagram = ValidAnagram

print(valid_anagram.isAnagram("anagram", "nagaram"))