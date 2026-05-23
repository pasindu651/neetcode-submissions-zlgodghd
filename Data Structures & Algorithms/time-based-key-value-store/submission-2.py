class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            items = self.data[key]
        else:
            return ""
        l = 0
        r = len(items) - 1
        closest = ""
        while(l <= r):
            m = (l+r) // 2
            if items[m][1] == timestamp:
                return items[m][0]
            elif items[m][1] < timestamp:
                closest = items[m][0]
                l = m + 1
            else:
                r = m - 1
        return closest