class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # 2 -> 3 -> 4 -> 5
        # 10 
        # 20
        numSet = set(nums)
        longest = 0 # Only need to keep track of current longest consecutive sequence
        for n in nums:
            if (n-1) not in numSet:
                # Start a new sequence
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest  


            