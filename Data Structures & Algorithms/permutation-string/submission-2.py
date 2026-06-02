class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        windowSize = len(s1)
        count_s1 = {}
        count_s2 = {}
        for charCode in range(ord('a'), ord('z') + 1):
            count_s1[chr(charCode)] = 0
            count_s2[chr(charCode)] = 0
        for c in s1:
            count_s1[c] = count_s1.get(c, 0) + 1
        l = 0
        for c in s2[0:windowSize]:
            count_s2[c] = count_s2.get(c, 0) + 1
        if count_s1 == count_s2:
            return True
        for r in range(windowSize, len(s2)):
            count_s2[s2[r - windowSize]] -= 1
            count_s2[s2[r]] += 1
            if count_s1 == count_s2:
                return True
        return False

         
        