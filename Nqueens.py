
def NQueens(board, n, loops, row, col):
    if isSafe(board, n, row, col):
        board[row][col] = 1   # Place queen
        printBoard(board)
        if loops == n+1:
            print("You win, perfect!")  
            return False
    else:
        board[row][col] = 1   # Place queen
        printBoard(board)
        print("You lose.")  
        return False
    return True
        

def isSafe(board, n, row, col):
    # Check column
    for i in range(n):
        if board[i][col] == 1:
            return False
        
    # Check row
    for i in range(n):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Check lower-right diagonal
    i, j = row, col
    while i <= n and j <= n:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1


    # Check upper-right diagonal
    i, j = row, col
    while i >= 0 and j <= n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    # Check lower-left diagonal
    i, j = row, col
    while i <= n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def printBoard(board):
    for i in range(n):
        for j in range(n):
            print("Q " if board[i][j] == 1 else ". ", end="")
        print()

# Main
while (True):
    n = int(input("Size of Board: "))
    board = [[0 for _ in range(n)] for _ in range(n)]
    row = -1
    col = -1
    loops = 0
    playing = True
    while (playing == True):
        loops += 1
        row = int(input("Row: "))
        while (row > n-1 or row < 0):
            row = int(input("Row: "))
        col = int(input("Column: "))
        while (col > n-1 or col < 0):
            col = int(input("Column: "))
        playing = NQueens(board, n-1, loops, row, col)