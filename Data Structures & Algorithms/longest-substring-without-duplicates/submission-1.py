class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        numSet = set()
        for r in range(len(s)):
            while s[r] in numSet: #while the new character still exists in the set
                numSet.remove(s[l])
                l += 1
            numSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
                