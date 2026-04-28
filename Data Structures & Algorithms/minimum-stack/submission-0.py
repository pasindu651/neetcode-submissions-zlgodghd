class MinStack:

    def __init__(self):
        self.data = [] # each element will be (val, min) where min is the minimum element at the time of pushing

    def push(self, val: int) -> None:
        if self.data:
            # compare val to minimum at the time of last push
            self.data.append((val, min(val, self.data[-1][1])))
        else:
            self.data.append((val, val))
    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.data[-1][1]
