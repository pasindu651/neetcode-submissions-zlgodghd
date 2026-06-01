class Solution:
    def isAlphanumeric(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or (ord('0') <= ord(c) <= ord('9')))
    def isPalindrome(self, s: str) -> bool:
        if(len(s) == 1):
            return True
        l = 0
        r = len(s) - 1
        while l <= r:
            while l < len(s) - 1 and not self.isAlphanumeric(s[l]):
                l += 1
            while r > 0 and not self.isAlphanumeric(s[r]):
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        