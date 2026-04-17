class Solution:
    def hasDuplicates(self, nums: List[str]) -> bool:
        nums = [n for n in nums if n!= '.']
        return len(set(nums)) != len(nums)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9): 
            row = board[i]
            col = [board[j][i] for j in range(9)]
            if self.hasDuplicates(row) or self.hasDuplicates(col):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3): #0, 3, 6, 9
                    # Every iteration of i, we begin at the top left corner of a sub_box
                    # Use r and c to grab all 9 cells within a sub_box
                    box = [board[i+r][j+c] for r in range(3) for c in range(3)]
                    if self.hasDuplicates(box):
                        return False
        return True 
