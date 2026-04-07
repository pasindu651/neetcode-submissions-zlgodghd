class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #stores indices
        for i, num in enumerate(nums):
            # y is compliment that was PREVIOUSLY seen
            y = target - num
            if y in seen:
                return [seen[y], i]
            seen[num] = i
        