class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            l = 0
            r = len(matrix[i]) - 1
            if target >= matrix[i][l] and target <= matrix[i][r]:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        return True
            else:
                continue
            
        return False

                