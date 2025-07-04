
def NQueens(board, n, row, col):
    i = 0
    if isSafe(board, row, col):
        board[row][col] = 1   # Place queen
        printBoard(board)
        i += 1
        if i == n:
            print("You win, perfect!")  
            return False
    else:
        board[row][col] = 1   # Place queen
        printBoard(board)
        print("You lose.")  
        return False
    return True
        

def isSafe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < 4:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
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
    playing = True
    while (playing == True):
        while (row > 3 or row < 0):
            row = int(input("Row: "))
        while (col > 3 or col < 0):
            col = int(input("Column: "))
        playing = NQueens(board, n, row, col)