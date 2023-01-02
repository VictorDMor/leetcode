'''
37. Sudoku Solver

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

Example 1:
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]
]
Explanation: The input board is shown above and the only valid solution is shown below:
'''
class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        def create_sub_box_board(board):
            x = 1
            sub_box_board = [[], [], [], [], [], [], [], [], []]
            for i in range(len(board)): # 9
                if i < 3:
                    k = 0
                elif i < 6:
                    k = 3
                else:
                    k = 6
                for j in range(len(board[i])): # 9
                    if j > 0 and j % 3 == 0:
                        k += 1
                    sub_box_board[i].append(board[k][j%3+((i%3)*3)])

            return sub_box_board

        def get_specific_sub_box(row, col):
            if col < 3:
                if row < 3:
                    return 0
                elif row < 6:
                    return 3
                else:
                    return 6
            elif col < 6:
                if row < 3:
                    return 1
                elif row < 6:
                    return 4
                else:
                    return 7
            else:
                if row < 3:
                    return 2
                elif row < 6:
                    return 5
                else:
                    return 8

        def check_solve_condition(board):
            solved = True
            for rows in board:
                for cell in rows:
                    if cell == '.':
                        solved = False
                        break
                if not solved:
                    break
            return solved

        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        solved = False
        ## To be continued tomorrow
        while not solved:
            sub_boxes = create_sub_box_board(board)
            for i in range(len(board)):
                for j in range(len(board[i])):
                    candidates = []
                    if board[i][j] != '.':
                        pass
                    else:
                        for n in numbers:
                            if n not in board[i] and n not in [x[j] for x in board] and n not in sub_boxes[get_specific_sub_box(i, j)]:
                                candidates.append(n)
                        print(candidates)
                        if len(candidates) == 1:
                            board[i][j] = candidates[0]
            if check_solve_condition(board):
                break
        return board


solution = Solution()
# print(solution.solveSudoku([
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]
# ]))
print(solution.solveSudoku([
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]))