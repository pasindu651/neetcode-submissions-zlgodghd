class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed)) # each item is a tuple (position, speed)
        stack = []
        for p,s in sorted(cars, reverse=True): # from closest to farthest to target
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # only keep fleets
        return len(stack)
