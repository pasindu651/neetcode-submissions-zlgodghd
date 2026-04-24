class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # sort input array first
        output = []
        for i, a in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            if i > 0 and a == nums[i-1]:
                continue # keep 'a' unique each time
            # a + b + c = 0
            # fix a and find b and c using two pointer algorithm
            while l < r:
                if (a + nums[l] + nums[r]) > 0:
                    r -= 1
                elif (a + nums[l] + nums[r]) < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    l += 1 # don't use same 'b'
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return output
