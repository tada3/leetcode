from typing import List

class Solution:
    @staticmethod
    def c2i(c):
        if c == '':
            return -1
        return ord(c) - 49
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = [[0 for _ in range(9)] for _ in range(9)]
        block = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]
        for i in range(len(board)):
            row = [0] * 9
            for j in range(len(board[i])):
                x = self.c2i(board[i][j])
                if x < 0:
                    continue
                if row[x] != 0:
                    return False
                row[x] = 1
                if column[j][x] != 0:
                    return False
                column[j][x] = 1
                bi = i // 3
                bj = j // 3
                if block[bi][bj][x] != 0:
                    return False
                block[bi][bj][x] = 1
        return True
    


def main(board):
    print(f'Input: board = {board}')
    ret = Solution().isValidSudoku(board)
    print(f'Output: {ret}')




if __name__ == "__main__":
    board = [
         ["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
    
    # board = [
    #      ["8","3",".",".","7",".",".",".","."]
    #     ,["6",".",".","1","9","5",".",".","."]
    #     ,[".","9","8",".",".",".",".","6","."]
    #     ,["8",".",".",".","6",".",".",".","3"]
    #     ,["4",".",".","8",".","3",".",".","1"]
    #     ,["7",".",".",".","2",".",".",".","6"]
    #     ,[".","6",".",".",".",".","2","8","."]
    #     ,[".",".",".","4","1","9",".",".","5"]
    #     ,[".",".",".",".","8",".",".","7","9"]]
    
    main(board)