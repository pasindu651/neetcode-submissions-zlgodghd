class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        if len(s2) < len(s1):
            return False
        for ascii_letter in range(ord('a'), ord('z') + 1):
            count_s1[chr(ascii_letter)] = 0
            count_s2[chr(ascii_letter)] = 0            
        for c in s1:
            count_s1[c] += 1

        if count_s1 == count_s2:
            return True

        for c in s2[:len(s1)]:
            count_s2[c] += 1

        if count_s1 == count_s2:
            return True
        for r in range(len(s1), len(s2)):
            count_s2[s2[r]] += 1 # add incoming character on right
            count_s2[s2[r - len(s1)]] -= 1 # evict left character from previous window
            if count_s1 == count_s2:
                return True
        return False