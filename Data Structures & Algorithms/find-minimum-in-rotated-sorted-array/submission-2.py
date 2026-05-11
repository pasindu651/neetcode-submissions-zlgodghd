class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minValue = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minValue = min(minValue, nums[l])
                break
            mid = (l+r)//2
            minValue = min(minValue, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return minValue