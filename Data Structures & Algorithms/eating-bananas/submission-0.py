import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # koko needs to eat at least one banana in an hour
        r = max(piles)
        # l and r define the range for our solution set for k
        k = r # initialize to worst case
        while l <= r:
            mid = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            if hours <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return k
            
