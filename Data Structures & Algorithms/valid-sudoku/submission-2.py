class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_block_valid(block):
            integer = [item for item in block if item.isdigit()]
            return len(integer) == len(set(integer))
            
    #for rows:
        for row in board:
            if not is_block_valid(row):
                return False
    #for columns:
        for col in range(len(board)):
            if not is_block_valid(board[row][col] for row in range(9)):
                return False
        # Check 3x3 sub-boxes
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block = [board[row][col] for row in range(box_row, box_row + 3) for col in range(box_col, box_col + 3)]
                if not is_block_valid(block):
                    return False
        
        return True

