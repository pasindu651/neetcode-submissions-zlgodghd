class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # perform binary search on the first element of each row to determine the correct row to search
        l = 0
        r = len(matrix) - 1
        index = -1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    index = mid
                    break
                l = mid + 1
            else:
                return True
        if index == -1:
            return False
        else:
            L = 0
            R = len(matrix[index]) - 1
            while L <= R:
                MID = (L+R) // 2
                if matrix[index][MID] > target:
                    R = MID - 1
                elif matrix[index][MID] < target:
                    L = MID + 1
                else:
                    return True
            return False
        

                