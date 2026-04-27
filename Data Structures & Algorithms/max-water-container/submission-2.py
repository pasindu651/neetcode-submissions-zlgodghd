class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0
        while l < r:
            area = (r - l)*min(heights[l], heights[r])
            maxArea = max(area, maxArea) 
            if heights[l] < heights[r]: #heights is not sorted so the next heights[l] or heights[r] could be smaller or larger
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: # doesn't matter - just increment either l or r
                l += 1
        return maxArea
