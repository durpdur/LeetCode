class Solution(object):
    def removeAllNonAlphaNum(self, string):
        return "".join(c for c in string if c.isalnum())
    def isPalindrome(self, s):
        if len(s) == 0 or len(s) == 1:
            return True
        l = 0
        r = len(s) - 1
        while l <= r:
            if not s[l].isalnum():
                l = l + 1
                continue
            if not s[r].isalnum():
                r = r - 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        
        return True

solution = Solution()

someString = "race a car"
print(solution.isPalindrome(someString))
print(solution.removeAllNonAlphaNum(someString))