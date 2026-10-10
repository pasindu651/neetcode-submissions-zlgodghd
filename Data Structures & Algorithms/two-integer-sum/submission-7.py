class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in visited:
                return [visited[difference], i]
            visited[n] = i

