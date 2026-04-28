class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for temp in temperatures]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                previous = stack.pop()
                output[previous[1]] = i - previous[1] # find difference in indices (number of days before warmer temp)
            stack.append((temp, i))
        return output