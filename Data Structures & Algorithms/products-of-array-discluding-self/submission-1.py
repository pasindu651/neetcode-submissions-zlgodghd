class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = []
        suffix_nums=[]
        for i in range(len(nums)):
            if i == 0:
                prefix_nums.append(1)
            else:
                prefix_nums.append(nums[i-1]*prefix_nums[i-1])
        for i in range(len(nums)-1, -1, -1):
            # Build suffix nums backwards
            if i == (len(nums)-1):
                suffix_nums.append(1)
            else:
                suffix_nums.append(nums[i+1]*suffix_nums[-1]) # Use last appended element of suffix_nums
        suffix_nums.reverse()
        output = [prefix_nums[i]*suffix_nums[i] for i in range(len(nums))]
        return output