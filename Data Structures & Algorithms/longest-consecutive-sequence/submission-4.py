class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        relationship = {} # {num:starting element}
        count = {} #{starting element: count of subsequence}
        numSet = set(nums)
        if len(nums) == 0:
            return 0
        for i,num in enumerate(nums):
            if (num-1) in numSet:
                smallestNum = num
                while (smallestNum - 1) in numSet:
                    smallestNum -= 1
                relationship[num] = smallestNum
            else:
                relationship[num] = num
        for num, start in relationship.items():
            count[start] = count.get(start, 0) + 1
        return max(count.values())
            