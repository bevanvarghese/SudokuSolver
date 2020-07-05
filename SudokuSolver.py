board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

def validMove(row, col, n):
    #check row
    for i in range(0,9):
        if board[row][i]==n:
            return False
    #check column
    for i in range(0,9):
        if board[i][col]==n:
            return False
    #check 3x3 box
    r_top = 3*(row//3)
    c_left = 3*(col//3)
    for i in [r_top, r_top+1, r_top+2]:
        for j in [c_left, c_left+1, c_left+2]:
            if board[i][j]==n:
                return False
    return True

def findEmpty():
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                #print(i,j)
                return [i,j]
    return False

def solve(board):
    found = findEmpty()
    if not found:
        return True
    row, col = found
    for n in range(1, 10):
        if validMove(row, col, n):
            board[row][col] = n
            if solve(board):
                return True
            #backtracking
            board[row][col] = 0
    return False

solve(board)
for i in range(9):
    print(board[i])
